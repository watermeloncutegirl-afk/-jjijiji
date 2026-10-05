# AI-automation Instagram: trend APIs, tooling and live trend snapshot

Prepared 2026-10-05. Niche: AI automation / AI tools for non-technical 25-34 professionals; offer about $3K B2B automation builds (for example a Vapi + Make.com + Airtable voice agent that calls leads and updates the CRM).

---

## 0. Platform rule that changes hashtag strategy

- **Instagram caps every post and Reel at 5 hashtags** (rolled out December 2025). Hashtag-following was removed in December 2024. Hashtags now mostly classify content; watch time and engagement drive reach. Source: [Later, updated 2026-04-21](https://later.com/blog/ultimate-guide-to-using-instagram-hashtags/).
- What to do: use about 1 broad, 2 mid and 2 niche tags per post, and put keywords in the caption and on-screen text (Instagram search indexes them).

---

## 1. APIs for trend, hashtag and topic data (status as of Oct 2026)

| Source | What you get | Cost | Auth / access | Status and caveats |
|---|---|---|---|---|
| **Instagram Graph API: Hashtag Search** (`ig_hashtag_search` -> `/{id}/top_media`, `/recent_media`, `recently_searched_hashtags`) | Hashtag ID; top or recent public posts with `like_count`, `comments_count`, `media_type`, `timestamp`, `permalink` (max 50 per page) | Free | IG Business or Creator account linked to a FB Page; Meta app with the **Instagram Public Content Access** feature plus `instagram_basic` (and `pages_read_engagement` or similar); user access token | **30 unique hashtags per rolling 7 days.** No total post count, no `username`, no Stories, no promoted posts, and sensitive tags return an error. [Meta docs: Hashtag Search](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-facebook-login/hashtag-search), [top_media](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-hashtag/top-media.md) |
| **Meta Content Library + API** | Full public archive of FB, IG and WhatsApp Channels (IG: verified accounts or 25K+ followers); 100+ fields | Not free from 2026: SOMAR charges research teams a monthly enclave fee | Application through Meta Research Tools Manager, reviewed by CASD; for academic and non-profit researchers only | **Not available to a creator or agency.** [Meta transparency page, updated 2026-04-30](https://transparency.meta.com/en-gb/researchtools/meta-content-library/) |
| **Apify Instagram actors** (`apify/instagram-hashtag-scraper`, `apify/instagram-scraper`, `instagram-reel-scraper`, `instagram-hashtag-stats`) | Posts per hashtag with likes, comments, captions, hashtags and timestamps; hashtag stats with post counts | Official hashtag scraper about **$2.30 per 1,000 results**; third-party actors about $1.50-$3.99 per 1K; free monthly platform credit | `APIFY_TOKEN` | Works without your own IG account; scraping is against IG terms, so the risk falls on Apify. [Apify search results](https://apify.com/scrapemesh/instagram-hashtag-scraper) |
| **RapidAPI Instagram wrappers** (Easy Instagram Service, Instagram Statistics API, and others) | Varies: hashtag media, counts, profiles | Free tiers of about 50 requests/day to 5K/month; paid about $10-$390/month | RapidAPI key | Quality and uptime vary by vendor; unofficial. [Xpoz 2026 pricing guide](https://www.xpoz.ai/blog/guides/instagram-api-pricing-2026/), [RapidAPI Easy Instagram Service](https://rapidapi.com/de/ariefsam/api/easy-instagram-service/pricing) |
| **Google Trends: unofficial** (`pytrends`, `trendspy`) | Interest over time, related or rising queries, trending now | Free | None | `pytrends` was **archived 2025-04-17** and often gets 429s. `trendspy` is maintained. Both are rate-limited ("quota exceeded" on related queries). [apiserpent](https://apiserpent.com/blog/pytrends-dead-google-trends-data-2026), [scrapebadger](https://scrapebadger.com/blog/does-google-trends-have-an-api-what-to-use-in-2026) |
| **Google Trends API (official, alpha)** | 5-year consistently scaled interest; day, week, month or year; region and sub-region | Not published | Application-gated alpha (announced 2025-07-24); no self-serve key | Still alpha in 2026; most developers cannot get in. [PPC Land](https://ppc.land/google-opens-alpha-testing-for-new-trends-api-targeting-developers-and-journalists/), [konabayev](https://konabayev.com/blog/google-trends-api-landscape-2026/) |
| **TikTok Creative Center** (cross-platform signal) | Trending hashtags by industry, region and period, with post and view counts | Free UI; no official public API (Apify wrappers cost about $1-5 per 1K) | None for the UI; Apify token for actors | June 2026 redesign **removed the public Videos, Creators and Songs trend feeds**; only hashtags by industry remain. The public endpoint caps at 3 hashtags per request. [Apify search results](https://apify.com/dami_studio/tiktok-creative-center-trends) |
| **Exploding Topics API** | Early-stage rising topics with growth curves | **$1,000/month for 1K requests** (to $4,000 for 25K), and needs the Pro Business plan ($249+/month) | API key | Too expensive for a new account; the free website is enough for scanning. [Exploding Topics API](https://explodingtopics.com/feature/et-api) |
| SerpApi / DataForSEO (Trends) | Reliable Google Trends JSON | Paid (about $50+/month SerpApi; DataForSEO pay as you go) | API key | Use these if the free Trends clients keep failing. |

**Recommendation:** use free Google Trends (trendspy) together with the IG Graph API from your own Creator account (spend the 30-tag budget carefully). Add Apify (about $5-10/month of credit) only if you need total post counts or engagement samples beyond the top 50 posts.

---

## 2. Script: `/home/user/-jjijiji/tools/ig_trends/`

- Files: `fetch_trends.py`, `README.md`, `requirements.txt`, `.gitignore` (ignores `output/`).
- Run: `pip install -r requirements.txt && python fetch_trends.py` (keys only from the env vars `IG_ACCESS_TOKEN`, `IG_USER_ID`, `APIFY_TOKEN`). Use `--offline` to skip the network, `--apify-stats` for live post counts, and `--post-counts file.json` for manual counts.
- **Test results (2026-10-05, venv in scratchpad):**
  - `--offline` runs cleanly.
  - Live Google Trends via `trendspy` **worked through the proxy** for interest-over-time on all 9 seeds.
  - Related queries repeatedly hit "quota exceeded" in `trendspy`. The script retries through `pytrends`, which did return data. Every failure is logged in the report's "Errors / degraded sources" section rather than crashing the run.
  - The IG and Apify code paths were tested with fake tokens. Requests reach the endpoints (Graph 400, Apify 401), the errors are captured, and tokens are redacted from messages.
  - They have **not** been tested with real credentials.
- Live Google Trends momentum on 2026-10-05 (worldwide, last 3 months, recent quarter of window vs earlier):

| Seed | Momentum |
|---|---|
| ai automation | 1.21 (rising) |
| ai tools | 1.19 (rising) |
| make.com | 1.10 |
| ai agents | 0.95 |
| ai voice agent | 0.95 |
| chatgpt | 0.89 |
| vapi | 0.84 |
| n8n | 0.80 |
| vibe coding | 0.79 (cooling) |

- Useful rising related searches seen on 2026-10-05:
  - "openclaw" and "openclaw vs n8n" (rising under n8n)
  - "google antigravity"
  - "google flow ai creative studio" (+8,000% under ai tools)
  - "best vibe coding tools"
  - "1980s photo prompt chatgpt" (+4,950%)
  - "chatgpt astra"
  - "consumer adoption of ai agents"
- Many rising lists for small terms were noise (for example "gardening" and "how to bake a cake"). The script filters these out of hashtag candidates.

---

## 3. Hashtag tiers (Instagram total posts)

Counts are third-party estimates, not read from Instagram. Instagram shows counts only when you are logged in, and the Graph API does not expose them. Treat these as orders of magnitude. **Sources disagree heavily**: best-hashtags.com shows #artificialintelligence at about 0.9M and #chatgpt at 10.6K (data from 2024), while iqhashtags shows 8.2M and 5.0M.

### Broad (>5M)
| Tag | Posts | Source / date |
|---|---|---|
| #ai | ~41.3M | iqhashtags.com, page dated 2026-10-05 |
| #automation | ~33.1M | iqhashtags.com headline (2026); **unverified**: the same number appears for #technology, so it may be a page artifact |
| #artificialintelligence | ~8.2M | iqhashtags.com 2026-10-05 (conflicts with displaypurposes.com at 894K, footer 2026-10-05) |
| #chatgpt | ~5.0M (borderline broad/mid) | iqhashtags.com 2026-10-05 (another iqhashtags snippet said 41.3M, which looks like a page bug) |
| #smallbusiness (adjacent) | ~156M | iqhashtags.com 2026-10-05 |
| #businesstips (adjacent) | ~8.6M | iqhashtags.com 2026-10-05 |

### Mid (100K-5M)
| Tag | Posts | Source / date |
|---|---|---|
| #leadgeneration | ~2.1M (best-hashtags: 561K, Oct 2024) | iqhashtags.com 2026-10-05 |
| #digitaltransformation | ~2.6M | iqhashtags.com 2026-10-05 |
| #openai | ~996K | iqhashtags.com 2026-10-05 |
| #aitools | ~783K | iqhashtags.com 2026-10-05 |
| #chatgpt4 | ~311K | iqhashtags.com 2026-10-05 |
| #crmsoftware | ~132K | iqhashtags.com 2026-10-05 |
| #crm | **unverified** (likely mid to broad) | none found |

### Niche (<100K)
| Tag | Posts | Source / date |
|---|---|---|
| #aitips | ~92K | iqhashtags.com 2026-10-05 |
| #nocode | ~26K (stale; probably higher now) | best-hashtags.com, data about 2024 |

### Could not verify (no reliable public count found as of 2026-10-05)
#aiautomation, #aiagents, #makecom, #n8n, #voiceai, #aireceptionist, #businessautomation, #salesautomation, #airtable, #smallbusinesstips, #aivoiceagent, #vibecoding.

Best guesses, all unverified:
- #aiautomation and #aiagents: likely mid
- #n8n, #makecom, #aireceptionist, #salesautomation, #businessautomation, #airtable, #voiceai: likely niche to low-mid

To get real counts, check each tag in the IG app or run `fetch_trends.py --apify-stats`.

**Warning on #vapi:** Vapi is also a city in Gujarat, India. Its hashtag and search interest are dominated by local news (Google rising searches on 2026-10-05: "vapi rains" and "vapi flood"). Avoid it; use #vapiai or name Vapi in the caption.

**Suggested 5-tag sets (one per post):**
- Voice-agent post: #aiautomation #aiagents #aireceptionist #smallbusinesstips #leadgeneration
- Tool tutorial: #aitools #n8n #makecom #nocode #aitips
- News or reaction: #chatgpt #aiagents #aitools #openai #aiautomation

---

## 4. Live AI topics right now (late Sep to early Oct 2026)

| Date | Topic | Source |
|---|---|---|
| 2026-09-29 | **OpenAI DevDay: "Dots"** are persistent agents on GPT-6 Astra that run on their own cloud computers and connect to thousands of apps. Also announced: ChatGPT Space (teammates plus agents) and "Pages" docs. Altman and Friar commented on the IPO. | [CNBC](https://cnbc.com/2026/09/29/openai-devday-2026-live-updates.html), [Manaknight weekly](https://manaknightdigital.com/blog/ai-news-week-of-october-02-2026) |
| 2026-09-28 | **Anthropic Claude Sonnet 5.5** ($2/$10 per M tokens). Claude Opus 5.5 launched 2026-09-22. Claude Chat and Cowork merged. IPO filing shows about $4.6B 2025 revenue; Anthropic is still planning a 2026 IPO. | [Manaknight](https://manaknightdigital.com/blog/ai-news-week-of-october-02-2026), [Hans India 2026-09-29](https://www.thehansindia.com/tech/upcoming-ai-updates-in-october-2026-major-developments-to-watch-1127036), [SiliconANGLE 2026-10-02](https://siliconangle.com/2026/10/02/despite-ipo-jitters-and-ai-safety-worries-anthropic-sticks-to-a-2026-offering/) |
| 2026-09-30 | **Google Gemini 4 Argon** (1M-token context; initially limited to cybersecurity partners). The broad Gemini 4 release is expected late 2026. Google ADK for Kotlin was also released. | Manaknight; Hans India; [aiagentstore weekly](https://aiagentstore.ai/ai-agent-news/this-week) |
| 2026-09-29 | **Robinhood trading agents** (OpenAI and Anthropic) rolled out to about 29M users. | [Fortune](https://fortune.com/2026/09/29/robinhood-trading-agents-hood-openai-anthropic/) |
| late Sep 2026 | **Agent safety and control**: NVIDIA Open Agent Safety Platform (OpenShell, Sentry). Voluntary US safety commitments signed. OpenAI reportedly paused training after agent security incidents. GPT-6.1 Astra reportedly delayed. | Manaknight; Hans India |
| Oct 2026 (expected) | iOS 27.1 and 27.2 Siri AI language expansion; possible Meta "Hatch" consumer-agent platform (unconfirmed) | Hans India 2026-09-29 |
| Sep 2026 | **"1980s AI photo" ChatGPT prompt trend** is viral on Instagram (strongest in India) | [Esquire India](https://www.esquireindia.co.in/tech-and-auto/gadgets/viral-1980s-ai-photo-trend-chatgpt-prompts-to-create-retro-photos-for-instagram), [Oman Observer 2026-09-12](https://www.omanobserver.om/article/1196004/scitech/technology/1980s-ai-photo-trend-going-viral) |
| 2026 ongoing | **OpenClaw vs n8n**: open-source chat-app agent paired with n8n, a hot comparison topic | [TechRadar](https://www.techradar.com/pro/n8n-vs-openclaw-what-are-the-differences-and-where-should-you-use-either-of-them), Google Trends rising 2026-10-05 |
| 2026 | **Voice AI for SMBs**: about 34% of US and EU SMBs use some AI phone handling (11% in 2024). The voice-agent sub-market is about $3.5B in 2026. These are vendor figures and **unverified**. | [growwstacks](https://growwstacks.com/blog/why-voice-ai-will-explode-in-2026/), [ainora](https://ainora.lt/blog/state-of-ai-voice-agents-report-2026) |

Content angles for the niche:
- "OpenAI just launched persistent agents (Dots). Here is what a small business can automate today without waiting."
- "I built the AI receptionist that calls your leads in 60 seconds (Vapi + Make + Airtable)."
- "OpenClaw vs n8n: which one should a non-technical owner use?"

---

## 5. Reel audio and format trends (Oct 2026)

- **"The Process" format** shows the tools and steps, then reveals the result (Nuelink, updated 2026-10-02; NewEngen). It fits voice-agent build walkthroughs best: screen recording of the Make scenario, then a phone ringing, then the Airtable row updating.
- **"My Reaction To ___"** uses escalating numbers ($10 to $2,000). Swap in "hours saved" or "leads called".
- **"Please keep me in your thoughts"** is a positioning format: "...as the person who automates your follow-ups" (Nuelink 2026-10-02).
- **Business-safe audio:** LuLuMusic "Autumn Colors" (about 55K Reels). Other trending audio is mostly pop: Taylor Swift "Patient Zero" (about 53K Reels), Ingrid Michaelson "Be OK" ("acting fine" meme, usable for "me pretending my CRM is up to date"). Source: [SocialPilot / Later / scottsocialmarketing roundup, Oct 2026](https://www.socialpilot.co/blog/instagram-reels-trends).
- Reel counts change weekly and were not verified in the app; check Instagram's "Trending" audio label before posting.

Sources for this section: [Nuelink, 2026-10-02](https://blog.nuelink.com/trending-on-instagram-october-2026/), [NewEngen](https://newengen.com/insights/instagram-trends/), [Later Reels trends](https://later.com/blog/instagram-reels-trends/), [Scott Social](https://www.scottsocialmarketing.com/blog/trending-reels-audio-this-week-on-instagram).
