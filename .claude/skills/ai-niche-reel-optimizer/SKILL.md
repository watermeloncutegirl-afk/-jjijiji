---
name: ai-niche-reel-optimizer
description: Write the caption, on-screen hook and 5 hashtags for an Instagram Reel in the user's AI-automation niche (25–34 non-technical professionals, B2B AI automation offer). Use when the user asks for a caption, description, hashtags, hook or CTA for a new Reel, or wants to pick the next Reel topic.
---

# AI-niche Reel optimizer

Applies the user's own niche research and the Oct 2026 Instagram rules. Read these first:
- `instagram/research/AI_Playground.csv`: topic rankings, hook families, audience
- `instagram/research/algorithm_report.md`: 2026 ranking rules with sources
- `instagram/research/trends_report.md`: hashtag tiers, APIs, live topics
- `instagram/first-reel-post-plan.md`: the worked example to copy the format of

For craft depth, the generic skills in this folder help: `viral-hooks`, `viral-captions-and-ctas`,
`viral-instagram-reels`, `hashtag-keyword-research`, `reel-scripter`.

## Step 1: Refresh trend data (optional)
`python tools/ig_trends/fetch_trends.py` (Google Trends is free; set `IG_ACCESS_TOKEN`+`IG_USER_ID`
or `APIFY_TOKEN` for Instagram data). Use the output's momentum to choose between candidate
tags/topics. Never invent post counts. Say "unverified" when no source exists.

## Step 2: Place the Reel in the user's framework
- **Topic:** map to one of the 10 ranked topics in the CSV. Prefer low-competition, fast-growth ones (AI automation for non-technical people, AI agents in real businesses, workplace deliverables).
- **Hook family:** prefer the bottom rows of the hook table (Niche Prompting, Build/Proof, Time Collapse). Avoid leaning on Income Proof or News for conversion.
- **Audience:** 25–34 working professionals who feel overwhelmed. Promise relief and a decision, not education.

## Step 3: Write the output
1. **Caption line 1:** the literal search phrase + tools/profession ("AI voice agent that calls your leads (Make.com + Vapi)"). No emojis before the keyword.
2. **Body (2–5 short lines):** the before → after flow, what it replaces, who it's for (name professions).
3. **One CTA:** save (tutorial/list) or send ("send this to the X who…"). No "comment WORD", "tag a friend" or "follow for more" while the account is under roughly 1K followers. Instagram demotes engagement bait.
4. **Exactly 5 hashtags** (hard cap since Dec 2025): 2 niche descriptors of the exact content, 1 tool tag, 1 buyer-side mid tag (e.g. #leadgeneration), 1 broad category. Never #viral/#fyp/#explore. Avoid ambiguous tags (#vapi means a city; use #vapiai).
5. **On-screen text:** 3–7 words repeating the caption keyword, visible on frame 1. The first frame shows the finished result.
6. **2–3 spoken hook options** from different hook families, for the user to A/B by 3-second retention.

## Guardrails
- Don't put unverifiable income or result claims in hooks for a new account.
- Check tool/model names in the script are real and current.
- Original footage only. No other platforms' watermarks.
