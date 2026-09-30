# Week 1: Setup

Goal: by the end of this week you have somewhere to track leads, alerts bringing people to you, a referral program people can join, and proof (case studies) to send them.
Time needed: **about 6–8 hours total**, spread over 5 days.

| File | What it is |
|---|---|
| [`lead-tracker.xlsx`](lead-tracker.xlsx) | Lead + partner tracker with a dashboard (import into Google Sheets) |
| [`referral-forms.gs`](referral-forms.gs) | Script that creates your Partner Sign-up form and Refer-a-Client form, already linked to the tracker |
| [`1-searches-and-alerts.md`](1-searches-and-alerts.md) | Exact searches, links and alert setup for LinkedIn, Facebook, F5Bot, Google Alerts, X |
| [`2-referral-terms.md`](2-referral-terms.md) | One-page partner terms (UK-based, worldwide partners), ready to paste into a Google Doc |
| [`3-case-studies.md`](3-case-studies.md) | Template for turning your 3+ past projects into case studies, plus the messages to send past clients |

---

## Decision 1: Platforms → LinkedIn + Facebook groups (plus Reddit alerts in the background)

- **LinkedIn:** business owners with real budgets, and the best place for AI automation deals.
- **Facebook groups:** where most "can anyone recommend a web designer?" posts appear, worldwide.
- **Reddit (passive):** F5Bot emails you when someone posts a matching request, so it takes no daily effort.
- Instagram, YouTube and Discord wait until month 2. They build an audience slowly and don't find buyers fast.

## Decision 2: Why the niche matters, and how to pick one

You said you target anyone, worldwide, who wants a website. **That's fine for replying to hire requests.** When someone posts "I need a website", you answer them whatever their industry. The niche matters for everything *else*:

1. **Your messages convert better.** "I build websites for plumbers, here's one that doubled their calls" beats "I build websites" every time. A generalist sounds like the other 20 replies under the post.
2. **Proof carries over.** A case study from a salon convinces the next salon. It barely moves a law firm.
3. **You can charge more.** Specialists get paid for knowing the industry (its booking tools, busy seasons, what customers ask). Generalists compete on price against Fiverr.
4. **Your content and searches get easier.** You know which groups to join, which hashtags to watch and what to post, instead of guessing.
5. **Referrals get easier.** Partners remember "the person who does websites for dentists." They forget "a web guy."

**Rule for picking yours: choose the industry of your best past project.** You already have proof there, which is the hardest part. If two are tied, pick the one where customers book appointments or call for quotes, because AI automation (bookings, missed-call text-back, chatbots) pays off most for them.

> **This week's setup:** reply to *any* hire request (generalist), but make your **posts, case studies and outbound messages** about **1 niche**. After 30 days, check the dashboard to see whether that niche closes better.

Write your pick here → **Niche: ____________________**

---

## Day-by-day plan

### Day 1: Tracker + forms (about 1.5h)
- [ ] Upload `lead-tracker.xlsx` to Google Drive → Open with Google Sheets.
- [ ] Delete the grey example rows on **Leads** and **Partners**.
- [ ] Check the numbers on **Settings** (commission %, cap, minimum deal). These are your choices, so change them if your margins are tighter.
- [ ] Extensions → Apps Script → paste `referral-forms.gs` → fill in `CONFIG` → Run `createReferralForms` → approve.
- [ ] Copy the two form links from the Settings tab. Test each form once yourself, then delete your test responses.

### Day 2: Referral terms (about 1h)
- [ ] Copy [`2-referral-terms.md`](2-referral-terms.md) into a Google Doc. Fill in the [brackets] and share it as "Anyone with the link can view".
- [ ] Put that Doc link into `CONFIG.termsUrl` and run the script again. (Or edit the forms' descriptions directly and delete the duplicate forms from the first run.)
- [ ] Write your partner-code convention: FIRSTNAME + 2 digits, e.g. JANE01.

### Day 3: Searches + alerts (about 1.5h)
- [ ] Follow [`1-searches-and-alerts.md`](1-searches-and-alerts.md): bookmark the LinkedIn and X search links, join 10–15 Facebook groups, set up F5Bot and Google Alerts.
- [ ] Make a browser bookmark folder called **Daily Hunt** containing all of them.

### Day 4–5: Case studies (about 2–3h)
- [ ] Fill in the template in [`3-case-studies.md`](3-case-studies.md) for your 3 best projects. Lead with the one in your chosen niche.
- [ ] Message those 3 past clients: ask permission, a testimonial, **and invite them to be referral partners** (script included).
- [ ] Turn each case study into a LinkedIn post (don't publish yet; that's Week 3) and a short version to paste into DMs.
- [ ] Update your LinkedIn headline + About section and your Facebook profile intro to mention your niche and the free audit offer.

### End of Week 1 check
- [ ] Tracker in Google Sheets with the forms linked
- [ ] Terms Doc published
- [ ] Daily Hunt bookmarks, 10+ FB groups joined, F5Bot + Google Alerts running
- [ ] 3 case studies written, 3 past clients messaged
- [ ] Profiles updated
- [ ] **First real leads logged.** You'll see a few while setting up the searches, so reply to them now; don't wait for Week 2.
