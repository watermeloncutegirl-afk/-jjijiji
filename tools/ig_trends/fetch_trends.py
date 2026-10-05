#!/usr/bin/env python3
"""
fetch_trends.py - find and score Instagram hashtags for the AI-automation niche.

Data sources (each one is optional and fails soft):
  1. Google Trends  - interest over time + top/rising related queries.
                      Uses `trendspy` if installed (maintained), else `pytrends`
                      (archived April 2025, often 429s). No key needed.
  2. Instagram Graph API - ig_hashtag_search -> top_media (like/comment counts).
                      Needs IG_ACCESS_TOKEN + IG_USER_ID (Business/Creator account
                      linked to a Meta app with Instagram Public Content Access).
                      Hard limit: 30 unique hashtags per rolling 7 days.
  3. Apify          - apify/instagram-hashtag-scraper (posts + engagement) and,
                      optionally, apify/instagram-hashtag-stats (total post count).
                      Needs APIFY_TOKEN. Paid per result.

Score per hashtag:
    score = relevance x engagement_per_post / log10(post_count)
log10 is used for "competition" so a 100K-post tag is not 1,000x better than a
100M-post tag; raw division would always crown near-empty tags.

All secrets are read from environment variables only.

Usage:
    python fetch_trends.py                       # default seeds, all sources available
    python fetch_trends.py --seeds "ai agents,n8n" --out ./output
    python fetch_trends.py --offline             # no network; reference data only
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import time
from typing import Any

try:
    import requests
except ImportError:  # requests is needed only for IG / Apify
    requests = None  # type: ignore

DEFAULT_SEEDS = [
    "ai automation", "ai agents", "ai tools", "vapi", "make.com", "n8n",
    "ai voice agent", "chatgpt", "vibe coding",
]

# Extra candidate hashtags always considered (curated for the niche/offer).
CURATED = [
    "aiautomation", "aiagents", "aitools", "automation", "nocode", "makecom",
    "n8n", "vapi", "voiceai", "aireceptionist", "smallbusinesstips",
    "businessautomation", "artificialintelligence", "chatgpt", "salesautomation",
    "leadgeneration", "crm", "airtable", "aivoiceagent", "vibecoding",
    "workflowautomation", "aiforbusiness", "openai", "aitips",
]

# Words that make a tag on-topic for the niche; used for relevance.
NICHE_TERMS = {
    "ai": 1.0, "agent": 1.0, "agents": 1.0, "automation": 1.0, "automate": 0.9,
    "voice": 0.9, "receptionist": 0.9, "workflow": 0.9, "nocode": 0.8, "n8n": 1.0,
    "make": 0.6, "makecom": 1.0, "vapi": 0.7, "airtable": 0.8, "crm": 0.8,
    "lead": 0.7, "leads": 0.7, "sales": 0.6, "business": 0.6, "chatgpt": 0.7,
    "openai": 0.6, "claude": 0.6, "artificialintelligence": 0.9, "intelligence": 0.7, "tools": 0.5, "coding": 0.5, "vibe": 0.5,
}

# Post-count snapshot (Instagram total posts) used only when no live count is
# available. Source + date are kept so the report can show provenance.
# Values marked None were not verifiable when this file was written.
REFERENCE_POST_COUNTS: dict[str, tuple[int | None, str]] = {
    "ai": (41_300_000, "iqhashtags.com, page dated 2026-10-05"),
    "chatgpt": (5_000_000, "iqhashtags.com, page dated 2026-10-05"),
    "artificialintelligence": (8_200_000, "iqhashtags.com, page dated 2026-10-05"),
    "aitools": (783_300, "iqhashtags.com, page dated 2026-10-05"),
    "openai": (995_600, "iqhashtags.com, page dated 2026-10-05"),
    "aitips": (91_900, "iqhashtags.com, page dated 2026-10-05"),
    "leadgeneration": (2_100_000, "iqhashtags.com, page dated 2026-10-05"),
    "crmsoftware": (131_800, "iqhashtags.com, page dated 2026-10-05"),
    "digitaltransformation": (2_600_000, "iqhashtags.com, page dated 2026-10-05"),
    "automation": (33_100_000, "iqhashtags.com headline (unverified, 2026)"),
    "nocode": (25_948, "best-hashtags.com (stale, ~2024)"),
}
UNKNOWN_POST_COUNT = 500_000  # neutral assumption when nothing is known


def log(msg: str) -> None:
    print(f"[fetch_trends] {msg}", file=sys.stderr)


def to_hashtag(text: str) -> str:
    """'make.com' -> 'makecom', 'AI voice agent' -> 'aivoiceagent'."""
    return re.sub(r"[^0-9a-z_]", "", text.lower())


# Navigational / off-topic words that make a related query useless as a hashtag.
NOISE = ("login", "signin", "signup", "download", "price", "pricing", "docs",
         "rain", "weather", "news", "mail", "stock", "share", "jobs", "salary",
         "apk", "free", "crack", "vs", "near", "city", "gujarat")

# Seeds/tags whose hashtag is polluted by another meaning (#vapi is also a city
# in Gujarat, India), so they get a capped relevance.
AMBIGUOUS = {"vapi": 0.4, "make": 0.3, "crm": 0.7}


def relevance(tag: str, seed_tags: set[str]) -> float:
    if tag in AMBIGUOUS:
        return AMBIGUOUS[tag]
    if any(n in tag for n in NOISE):
        return 0.1
    if tag in seed_tags:
        return 1.0
    score = 0.0
    for term, w in NICHE_TERMS.items():
        if term == "ai":
            # "ai" only counts as a prefix/suffix (aiagents, chatgptai), never
            # inside words like "rains" or "email"
            hit = tag.startswith("ai") or tag.endswith("ai")
        elif len(term) <= 3:
            hit = tag.startswith(term) or tag.endswith(term)
        else:
            hit = term in tag
        if hit:
            score = w if score == 0 else min(1.0, max(score, w) + min(score, w) * 0.25)
    return round(max(score, 0.2), 3)


# --------------------------------------------------------------------------
# Google Trends
# --------------------------------------------------------------------------
def google_trends(seeds: list[str], geo: str, timeframe: str) -> dict[str, Any]:
    out: dict[str, Any] = {"backend": None, "interest": {}, "related": {}, "errors": []}
    client = None
    try:
        from trendspy import Trends  # type: ignore
        client = ("trendspy", Trends(request_delay=2.0))
    except Exception:
        try:
            from pytrends.request import TrendReq  # type: ignore
            client = ("pytrends", TrendReq(hl="en-US", tz=0, timeout=(10, 25)))
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"no Google Trends library installed: {e}")
            return out
    name, c = client
    out["backend"] = name
    ref = {"referer": "https://www.google.com/"}

    def series_momentum(values: list[float]) -> dict[str, float]:
        vals = [float(v) for v in values if v is not None]
        if len(vals) < 8:
            return {"latest_avg": sum(vals) / max(len(vals), 1), "momentum": 1.0}
        k = max(len(vals) // 4, 1)
        recent = sum(vals[-k:]) / k
        prior = sum(vals[:-k]) / max(len(vals) - k, 1)
        return {"latest_avg": round(recent, 2), "momentum": round((recent + 1) / (prior + 1), 3)}

    def short(e: Exception) -> str:
        return f"{type(e).__name__}: {' '.join(str(e).split())[:140]}"

    # Interest over time, one keyword per request so each series is scaled to
    # itself (in a shared request "chatgpt" flattens everything else to 0).
    for kw in seeds:
        try:
            if name == "trendspy":
                df = c.interest_over_time([kw], timeframe=timeframe, geo=geo)
            else:
                c.build_payload([kw], timeframe=timeframe, geo=geo)
                df = c.interest_over_time()
            if df is not None and kw in df.columns:
                out["interest"][kw] = series_momentum(df[kw].tolist())
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"interest_over_time '{kw}': {short(e)}")
        time.sleep(1.5)

    # Related queries (rate-limited hardest), one seed at a time. On failure,
    # retry once - via pytrends if available, since its request path differs.
    py = None
    try:
        from pytrends.request import TrendReq  # type: ignore
        py = c if name == "pytrends" else TrendReq(hl="en-US", tz=0, timeout=(10, 25))
    except Exception:  # noqa: BLE001
        pass
    for kw in seeds:
        for attempt in (1, 2):
            try:
                if name == "trendspy" and not (attempt == 2 and py is not None):
                    rq = c.related_queries(kw, timeframe=timeframe, geo=geo, headers=ref)
                else:
                    p = py or c
                    p.build_payload([kw], timeframe=timeframe, geo=geo)
                    rq = p.related_queries().get(kw, {}) or {}
                rel: dict[str, list] = {}
                for part in ("top", "rising"):
                    df = rq.get(part) if hasattr(rq, "get") else None
                    if df is not None and len(df):
                        rel[part] = [
                            {"query": str(r["query"]), "value": str(r["value"])}
                            for _, r in df.head(15).iterrows()
                        ]
                out["related"][kw] = rel
                break
            except Exception as e:  # noqa: BLE001
                if attempt == 2:
                    out["errors"].append(f"related_queries '{kw}': {short(e)}")
                else:
                    time.sleep(8.0)
        time.sleep(3.0)
    return out


# --------------------------------------------------------------------------
# Instagram Graph API
# --------------------------------------------------------------------------
def instagram_graph(tags: list[str], max_tags: int) -> dict[str, Any]:
    token, user_id = os.environ.get("IG_ACCESS_TOKEN"), os.environ.get("IG_USER_ID")
    out: dict[str, Any] = {"enabled": bool(token and user_id), "tags": {}, "errors": []}
    if not out["enabled"]:
        return out
    if requests is None:
        out["errors"].append("requests not installed")
        return out
    ver = os.environ.get("IG_GRAPH_VERSION", "v24.0")
    base = f"https://graph.facebook.com/{ver}"
    log(f"Instagram Graph API: querying {min(len(tags), max_tags)} hashtags "
        "(each new tag uses 1 of your 30 unique hashtags per 7 days)")
    for tag in tags[:max_tags]:
        try:
            r = requests.get(f"{base}/ig_hashtag_search",
                             params={"user_id": user_id, "q": tag, "access_token": token},
                             timeout=30)
            r.raise_for_status()
            data = r.json().get("data") or []
            if not data:
                out["errors"].append(f"#{tag}: not found")
                continue
            hid = data[0]["id"]
            m = requests.get(f"{base}/{hid}/top_media",
                             params={"user_id": user_id, "limit": 50, "access_token": token,
                                     "fields": "id,like_count,comments_count,media_type,timestamp,permalink"},
                             timeout=30)
            m.raise_for_status()
            media = m.json().get("data") or []
            eng = [(x.get("like_count") or 0) + (x.get("comments_count") or 0) for x in media]
            out["tags"][tag] = {
                "hashtag_id": hid,
                "top_media_n": len(media),
                "avg_engagement_top": round(sum(eng) / len(eng), 1) if eng else None,
                "median_engagement_top": sorted(eng)[len(eng) // 2] if eng else None,
                "video_share": round(sum(1 for x in media if x.get("media_type") == "VIDEO") / len(media), 2) if media else None,
                "sample": [x.get("permalink") for x in media[:3]],
            }
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            if token:
                msg = msg.replace(token, "***")
            out["errors"].append(f"#{tag}: {type(e).__name__}: {msg[:200]}")
    return out


# --------------------------------------------------------------------------
# Apify
# --------------------------------------------------------------------------
def _apify_run(actor: str, payload: dict, token: str, timeout: int = 300) -> list[dict]:
    url = f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items"
    r = requests.post(url, params={"timeout": timeout}, json=payload,
                      headers={"Authorization": f"Bearer {token}"}, timeout=timeout + 30)
    r.raise_for_status()
    return r.json()


def apify(tags: list[str], per_tag: int, with_stats: bool) -> dict[str, Any]:
    token = os.environ.get("APIFY_TOKEN")
    out: dict[str, Any] = {"enabled": bool(token), "tags": {}, "post_counts": {}, "errors": []}
    if not token:
        return out
    if requests is None:
        out["errors"].append("requests not installed")
        return out
    actor = os.environ.get("APIFY_HASHTAG_ACTOR", "apify~instagram-hashtag-scraper")
    log(f"Apify {actor}: {len(tags)} tags x {per_tag} posts (paid per result)")
    try:
        items = _apify_run(actor, {"hashtags": tags, "resultsLimit": per_tag}, token)
        buckets: dict[str, list[int]] = {t: [] for t in tags}
        for it in items:
            src = str(it.get("inputUrl") or it.get("input") or "").lower()
            m = re.search(r"/tags/([^/?#]+)", src)
            key = m.group(1) if m else None
            if key not in buckets:  # fall back to the post's own hashtags
                own = {to_hashtag(h) for h in (it.get("hashtags") or [])}
                key = next((t for t in tags if t in own), None)
            if key is None:
                continue
            likes = it.get("likesCount") or 0
            likes = 0 if likes < 0 else likes  # hidden likes come back as -1
            buckets[key].append(likes + (it.get("commentsCount") or 0))
        for t, eng in buckets.items():
            if eng:
                out["tags"][t] = {"posts_sampled": len(eng),
                                  "avg_engagement": round(sum(eng) / len(eng), 1),
                                  "median_engagement": sorted(eng)[len(eng) // 2]}
    except Exception as e:  # noqa: BLE001
        out["errors"].append(f"{actor}: {type(e).__name__}: {str(e).replace(token, '***')[:200]}")
    if with_stats:
        stats_actor = os.environ.get("APIFY_STATS_ACTOR", "apify~instagram-hashtag-stats")
        try:
            items = _apify_run(stats_actor, {"hashtags": tags}, token)
            for it in items:
                name = to_hashtag(str(it.get("name") or it.get("hashtag") or ""))
                cnt = it.get("postsCount") or it.get("mediaCount") or it.get("posts")
                if name and isinstance(cnt, (int, float)):
                    out["post_counts"][name] = int(cnt)
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"{stats_actor}: {type(e).__name__}: {str(e).replace(token, '***')[:200]}")
    return out


# --------------------------------------------------------------------------
# Scoring + report
# --------------------------------------------------------------------------
def tier(n: int | None) -> str:
    if n is None:
        return "unknown"
    if n > 5_000_000:
        return "broad (>5M)"
    if n >= 100_000:
        return "mid (100K-5M)"
    return "niche (<100K)"


def build(seeds: list[str], extra: list[str], gt: dict, ig: dict, ap: dict,
          user_counts: dict[str, int]) -> list[dict]:
    seed_tags = {to_hashtag(s) for s in seeds}
    cands: dict[str, dict] = {}

    def add(tag: str, origin: str, boost: float = 1.0) -> None:
        if not tag or len(tag) < 2 or len(tag) > 40:
            return
        c = cands.setdefault(tag, {"tag": tag, "origins": set(), "trend_boost": 1.0})
        if tag in AMBIGUOUS:
            boost = min(boost, 1.0)  # search interest is not niche interest
        c["origins"].add(origin)
        c["trend_boost"] = max(c["trend_boost"], boost)

    for s in seeds:
        mom = gt.get("interest", {}).get(s, {}).get("momentum", 1.0)
        add(to_hashtag(s), "seed", min(max(mom, 0.5), 2.0))
    for t in CURATED + extra:
        add(to_hashtag(t), "curated")
    for kw, rel in gt.get("related", {}).items():
        for part, rows in rel.items():
            for r in rows[:8]:
                q = r["query"]
                if len(q.split()) > 3:
                    continue
                tag = to_hashtag(q)
                if relevance(tag, seed_tags) < 0.5:
                    continue  # off-topic or navigational query
                boost = 1.3 if part == "rising" else 1.0
                add(tag, f"google_{part}:{kw}", boost)

    rows = []
    for tag, c in cands.items():
        rel = relevance(tag, seed_tags)
        # engagement per post: Apify sample beats IG top_media (top media is biased high)
        eng, eng_src = None, None
        if tag in ap.get("tags", {}):
            eng, eng_src = ap["tags"][tag]["median_engagement"], "apify_median"
        elif tag in ig.get("tags", {}) and ig["tags"][tag]["median_engagement_top"] is not None:
            eng, eng_src = ig["tags"][tag]["median_engagement_top"], "ig_top_media_median"
        # post count / competition
        if tag in ap.get("post_counts", {}):
            pc, pc_src = ap["post_counts"][tag], "apify_stats (live)"
        elif tag in user_counts:
            pc, pc_src = user_counts[tag], "--post-counts file"
        elif tag in REFERENCE_POST_COUNTS and REFERENCE_POST_COUNTS[tag][0]:
            pc, pc_src = REFERENCE_POST_COUNTS[tag]
        else:
            pc, pc_src = None, "unknown"
        comp = math.log10(max(pc or UNKNOWN_POST_COUNT, 10))
        eng_val = eng if eng is not None else 1.0  # neutral when unknown
        score = rel * c["trend_boost"] * (math.log1p(eng_val) if eng is not None else 1.0) / comp
        rows.append({
            "hashtag": f"#{tag}", "score": round(score, 4), "relevance": rel,
            "trend_boost": round(c["trend_boost"], 3),
            "engagement_per_post": eng, "engagement_source": eng_src,
            "post_count": pc, "post_count_source": pc_src, "tier": tier(pc),
            "origins": sorted(c["origins"]),
        })
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows


def write_reports(out_dir: str, payload: dict) -> tuple[str, str]:
    os.makedirs(out_dir, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M")
    jp = os.path.join(out_dir, f"ig_trends_{stamp}.json")
    mp = os.path.join(out_dir, f"ig_trends_{stamp}.md")
    with open(jp, "w") as f:
        json.dump(payload, f, indent=2, default=list)
    s = payload["sources"]
    L = [f"# Instagram hashtag trends - {payload['generated_at']}", "",
         f"Seeds: {', '.join(payload['seeds'])}", "",
         "## Sources", "",
         f"- Google Trends: backend={s['google_trends'].get('backend')}, "
         f"errors={len(s['google_trends'].get('errors', []))}",
         f"- Instagram Graph API: {'on' if s['instagram_graph']['enabled'] else 'off (set IG_ACCESS_TOKEN + IG_USER_ID)'}",
         f"- Apify: {'on' if s['apify']['enabled'] else 'off (set APIFY_TOKEN)'}", "",
         "## Top hashtags", "",
         "| # | Hashtag | Score | Relevance | Trend boost | Eng/post | Posts | Tier | Count source |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(payload["hashtags"][:40], 1):
        pc = f"{r['post_count']:,}" if r["post_count"] else "?"
        eng = r["engagement_per_post"] if r["engagement_per_post"] is not None else "?"
        L.append(f"| {i} | {r['hashtag']} | {r['score']} | {r['relevance']} | {r['trend_boost']} | "
                 f"{eng} | {pc} | {r['tier']} | {r['post_count_source']} |")
    gt = s["google_trends"]
    if gt.get("interest"):
        L += ["", "## Google Trends momentum (last quarter of window vs earlier)", "",
              "| Keyword | Recent avg | Momentum |", "|---|---|---|"]
        for k, v in sorted(gt["interest"].items(), key=lambda kv: -kv[1]["momentum"]):
            L.append(f"| {k} | {v['latest_avg']} | {v['momentum']} |")
    if gt.get("related"):
        L += ["", "## Rising related searches", ""]
        for k, rel in gt["related"].items():
            rising = ", ".join(f"{r['query']} ({r['value']})" for r in rel.get("rising", [])[:6])
            if rising:
                L.append(f"- **{k}**: {rising}")
    errs = [e for src in s.values() for e in src.get("errors", [])]
    if errs:
        L += ["", "## Errors / degraded sources", ""] + [f"- {e}" for e in errs]
    L += ["", "_Score = relevance x trend_boost x log(1+engagement/post) / log10(post_count)._",
          "_Instagram allows max 5 hashtags per post/Reel (since Dec 2025): pick 1 broad, 2 mid, 2 niche._"]
    with open(mp, "w") as f:
        f.write("\n".join(L) + "\n")
    return jp, mp


def main() -> int:
    ap_ = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap_.add_argument("--seeds", help="comma-separated seed keywords")
    ap_.add_argument("--hashtags", default="", help="extra comma-separated hashtags to score")
    ap_.add_argument("--geo", default="", help="Google Trends geo, e.g. US (default: worldwide)")
    ap_.add_argument("--timeframe", default="today 3-m", help="Google Trends timeframe")
    ap_.add_argument("--ig-max", type=int, default=int(os.environ.get("IG_MAX_HASHTAGS", 20)),
                     help="max hashtags to query on IG Graph API (30/7-day budget)")
    ap_.add_argument("--apify-per-tag", type=int, default=30)
    ap_.add_argument("--apify-stats", action="store_true", help="also run apify hashtag-stats for post counts")
    ap_.add_argument("--post-counts", help="JSON file {hashtag: post_count} to override reference counts")
    ap_.add_argument("--top", type=int, default=25, help="how many top tags to send to IG/Apify")
    ap_.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    ap_.add_argument("--offline", action="store_true", help="skip all network calls")
    a = ap_.parse_args()

    seeds = [s.strip() for s in (a.seeds.split(",") if a.seeds else DEFAULT_SEEDS) if s.strip()]
    extra = [h.strip().lstrip("#") for h in a.hashtags.split(",") if h.strip()]
    user_counts: dict[str, int] = {}
    if a.post_counts:
        with open(a.post_counts) as f:
            user_counts = {to_hashtag(k): int(v) for k, v in json.load(f).items()}

    empty = {"enabled": False, "tags": {}, "post_counts": {}, "errors": []}
    if a.offline:
        gt = {"backend": None, "interest": {}, "related": {}, "errors": ["offline mode"]}
    else:
        log("Google Trends ...")
        gt = google_trends(seeds, a.geo, a.timeframe)
        for e in gt["errors"]:
            log(f"  degraded: {e}")

    prelim = build(seeds, extra, gt, empty, empty, user_counts)
    shortlist = [r["hashtag"][1:] for r in prelim[: a.top]]
    ig = empty if a.offline else instagram_graph(shortlist, a.ig_max)
    apy = empty if a.offline else apify(shortlist, a.apify_per_tag, a.apify_stats)
    rows = build(seeds, extra, gt, ig, apy, user_counts)

    payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "seeds": seeds,
        "sources": {"google_trends": gt, "instagram_graph": ig, "apify": apy},
        "hashtags": rows,
    }
    jp, mp = write_reports(a.out, payload)
    log(f"wrote {jp}")
    log(f"wrote {mp}")
    print("\nTop 10:")
    for r in rows[:10]:
        print(f"  {r['hashtag']:<28} score={r['score']:<7} tier={r['tier']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
