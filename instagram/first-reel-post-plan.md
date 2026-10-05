# First Reel — AI Voice Agent (Vapi + Make.com + Airtable)

Built on: your AI_Playground research (`research/AI_Playground.csv`), the 2026 algorithm
report (`research/algorithm_report.md`) and the live trends report (`research/trends_report.md`).
All dated 2026-10-05.

## 1. Caption (copy-paste)

```
AI voice agent that calls your new leads for you (Make.com + Vapi + Airtable)

A lead fills out your form → AI checks if they're qualified → Vapi calls them and has a real conversation → the call summary and "interested: yes/no" land in your CRM automatically.

No answer? It emails them and pings your sales team in Slack. No lead slips through the cracks.

What it replaces: someone dialing every form fill by hand, taking notes, then updating the CRM.

Built for agencies, clinics, law firms and home-service businesses that pay for leads that go cold before anyone calls.

Save this for the workflow map 📌
Send it to a business owner who's still calling leads by hand.

#aiautomation #aivoiceagent #makecom #leadgeneration #artificialintelligence
```

### Why it's written this way
| Choice | Reason |
|---|---|
| First line = search phrase, tools named | Instagram search indexes captions; public pro-account Reels are on Google since Jul 2025. "AI voice agent" + tool names = what a 25–34 professional actually types. |
| Arrow flow in line 2 | Your **Build/Proof** hook family (highest conversion) + **Explicit Transformation**: the caption itself is the deliverable, which drives saves. |
| "What it replaces" | Your teardown pillar (#2, "companies using AI"): show the workflow + what it replaced. Also fixes your own note that the script doesn't say *why* owners pay for it. |
| Named professions | Your **Niche-scoping** row: lowest competition, highest conversion. "Specificity is the moat." |
| Save + Send CTA, no "Comment AGENT" | Sends-per-reach is a top-3 ranking signal and the strongest one for non-followers (Mosseri, Jan 2025). Instagram has said it won't recommend posts asking people to comment a specific word. Bring "Comment AGENT" back once you have followers and a ManyChat flow — on post #1 it costs more reach than it earns. |
| No income claim | Your table rates **Income Proof** "Low (trust issues)". On a 0-follower account a "$10,000" claim reads as a pitch. Keep it for later, once proof exists on the grid. |

## 2. Hashtags — exactly 5 (Instagram's cap since Dec 2025)

| Tag | Tier | Role |
|---|---|---|
| #aiautomation | niche/mid (count unverified) | Your #1 topic, "how to learn ai automation", ▲1000%+, Google Trends momentum 1.21 (rising) |
| #aivoiceagent | niche (count unverified) | Exact description of the reel — tells Instagram what it is |
| #makecom | niche (count unverified) | Tool tag; make.com momentum 1.10 (rising). Use this, **not #vapi** (that's mostly a city in Gujarat) |
| #leadgeneration | mid (~2.1M) | Buyer-side tag — business owners, not AI hobbyists |
| #artificialintelligence | broad (~8.2M) | One broad category signal |

Hashtags don't add reach on their own anymore (Mosseri, Feb 2025); they classify the post. That's why
all 5 describe the content and none are #viral / #fyp / #explore.
Before posting, tap each niche tag in the app to confirm it's active and on-topic. Or run
`python tools/ig_trends/fetch_trends.py --apify-stats` with an `APIFY_TOKEN` to get real counts.

Rotation pool for later posts: #aiagents, #aitools (~783K), #nocode, #businessautomation, #crmsoftware (~132K), #aitips (~92K), #vapiai.

## 3. On-screen text & hook (first 1–3 seconds)

Per your **Result First** rule ("proof must be visible in the first second"):

- **First frame:** the Airtable row flipping to `Interested: ✅` with the call summary filled in. Not your face, not the Make canvas.
- **On-screen text (3–7 words, readable muted):** `AI voice agent calls your leads` — matches caption line 1 (keyword repeated = stronger classification).
- **Spoken hook options** (film 2–3, keep the one with the best 3-second hold):
  1. *Build/Proof:* "This AI just called a lead, qualified them, and updated my CRM — nobody touched it."
  2. *Time Collapse:* "Your leads go cold in the hour before anyone calls them. This calls them in seconds."
  3. *For X use Y:* "If you run an agency and pay for leads, this is the automation you need."

Keep text out of the top ~220px and bottom ~450px. Keep cover text inside the centre 3:4 crop.

## 4. Script tweaks (from your own "what's missing" notes)

- Swap the `$10,000` opener for hook 1 or 2 above. Use the income line later as a supporting fact, if at all.
- Add one line on **why owners pay**: "Every lead that waits an hour is a lead your competitor calls first. This is that missing salesperson, 24/7."
- Spell out Vapi's value in one line: "It doesn't read a script. It listens, asks follow-ups, and decides if they're a fit."
- Check the model name: the script says "ChatGPT 4.2". Use whatever your Vapi assistant is actually configured with; a wrong model name gets called out in comments.
- End with: "Save this, and send it to someone still calling leads by hand. Part 2: the exact Make scenario." That drives saves and sends now, and follows later.
- Length: aim for 45–60s. Under 3 minutes stays eligible for recommendation, but completion rate matters more.

## 5. Before you post (new account)

- Switch to a **public Creator or Business** account (needed for Google indexing and Insights).
- **Name field** (searchable, 30 chars): `YourName | AI Automation`
- **Bio (136/150 chars):**
  ```
  AI automation for people who aren't technical
  Stop testing every tool. Learn the few that save you hours
  Free templates + AI community 👇
  ```
  Link = your free Skool community. Pin 3 Reels: one tip, one build, one "what's inside the Skool".
- Use original footage and original voice. No CapCut/TikTok watermarks (originality rules tightened Apr 2026).
- Post Wed/Thu evening if you can. Timing matters little at 0 followers.
- No "warm-up" ritual needed. Don't mass-follow or mass-like (spam blocks).
- Plan 2 more Reels on the same pillar soon after (e.g. "Part 2: the Make scenario", "For law firms use this…"), then pin the best 3, so profile visitors see a clear niche.

## 6. Topical follow-ups (reach plays, decay fast)

From the 2026-10-05 trends sweep: OpenAI DevDay "always-on agents" (Sep 29), Robinhood AI trading agents (Sep 29),
"OpenClaw vs n8n" rising searches. Your **News/Reactive** row says reach only, so tie each one back to a build:
"OpenAI just launched always-on agents — here's one I already run for a client."
