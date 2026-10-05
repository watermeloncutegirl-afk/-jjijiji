# ig_trends - hashtag finder for the AI-automation niche

`fetch_trends.py` collects trend signals for your seed keywords, scores candidate
Instagram hashtags and writes a JSON + Markdown report to `./output/`.

## Install

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python fetch_trends.py                          # default seeds (ai automation, ai agents, ai tools, vapi, make.com, n8n, ai voice agent, chatgpt, vibe coding)
python fetch_trends.py --seeds "ai receptionist,airtable" --hashtags "dentistmarketing,hvacbusiness"
python fetch_trends.py --geo US --timeframe "today 1-m"
python fetch_trends.py --offline                # no network; uses the built-in reference post counts
python fetch_trends.py --post-counts counts.json   # {"aiagents": 812000, ...} counts you read off Instagram yourself
```

Takes 1-3 minutes (deliberate pauses between Google Trends calls).

## Data sources and keys (environment variables only - never hardcode)

| Source | Needed | What it adds | Cost |
|---|---|---|---|
| Google Trends (`trendspy`, fallback `pytrends`) | nothing | 3-month momentum per seed; top/rising related searches become candidate tags | free, rate-limited (429 / "quota exceeded" is common; the script logs it and carries on) |
| Instagram Graph API | `IG_ACCESS_TOKEN`, `IG_USER_ID` (optional `IG_GRAPH_VERSION`, default `v24.0`; `IG_MAX_HASHTAGS`, default 20) | like + comment counts of each hashtag's top 50 posts | free; needs a Business/Creator IG account linked to a Facebook Page and a Meta app with *Instagram Public Content Access*. **30 unique hashtags per rolling 7 days** - the script caps queries at `--ig-max`. The API does **not** return a hashtag's total post count. |
| Apify | `APIFY_TOKEN` (optional `APIFY_HASHTAG_ACTOR`, `APIFY_STATS_ACTOR`) | median engagement from `apify/instagram-hashtag-scraper`; with `--apify-stats`, live total post counts from `apify/instagram-hashtag-stats` | pay per result (about $2.30 per 1,000 posts for the hashtag scraper in 2026) |

```bash
export IG_ACCESS_TOKEN=...   # long-lived user token
export IG_USER_ID=...        # IG Business account id (not the @handle)
export APIFY_TOKEN=...
python fetch_trends.py --apify-stats --apify-per-tag 20
```

## Scoring

```
score = relevance x trend_boost x log(1 + engagement_per_post) / log10(post_count)
```

- **relevance** (0-1): 1.0 for seed tags, otherwise keyword match against a niche list. Navigational
  queries ("make.com login", "vapi rain") are dropped; `#vapi` is capped at 0.4 because it is also a city
  in Gujarat, India, so the tag is full of local news.
- **trend_boost**: Google Trends momentum for seeds (recent quarter vs earlier, clamped 0.5-2), 1.3 for
  rising related searches.
- **engagement_per_post**: Apify median if available, else IG top-media median (biased high), else neutral.
- **post_count**: Apify stats > `--post-counts` file > built-in snapshot (`REFERENCE_POST_COUNTS`, with
  source and date) > assumed 500K. log10 dampens competition so a near-empty tag does not win
  automatically.

Instagram allows at most **5 hashtags per post/Reel** (since Dec 2025). Pick about 1 broad (>5M),
2 mid (100K-5M) and 2 niche (<100K) tags from the report.

## Known limits

- Google Trends "rising" lists for small terms are noisy (unrelated searches such as "gardening" show up);
  the relevance filter keeps them out of the hashtag list, but read the Markdown section with care.
- The built-in post counts come from third-party sites, not Instagram itself, and some are stale. Refresh
  them with `--apify-stats` or a `--post-counts` file before relying on tiers.
