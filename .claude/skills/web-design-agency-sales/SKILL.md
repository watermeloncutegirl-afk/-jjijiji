---
name: web-design-agency-sales
description: Runs the demo-first sales pipeline for a local-business web design agency (Vanguard Studios model), from Google Maps lead list to prospect audit, demo build brief, outreach sequence, closer demo-call agenda, proposal one-pager and kick-off checklist. Use when the user asks to "build a lead list" for a niche and city, "audit this prospect", "write a demo brief", "write a cold email or follow-up sequence for a local business", "prep the demo call", "write a proposal" or "onboard a new website client", or mentions selling websites to salons, trades, restaurants, gyms, auto shops or other local businesses.
---

# Web Design Agency Sales (demo-first)

The Vanguard model: **build the demo before anyone dials.** "We already built you a demo" is the hook in every opener, so it must be literally true. No demo, no call.

## Pipeline

```
1. Lead list      niche + city, Google Maps, qualify on signals
2. Prospect audit verified facts only: costing / fix / caught our eye
3. Demo brief     pages, copy from their reviews & listing, CTA, booking
4. Build demo     (designer/dev; frontend-design skill if building with Claude)
5. Outreach       call first (sibling skills), then compliant email + voicemail cadence
6. Demo call      [Closer] runs 15–30 min agenda, gives exact price
7. Proposal       one page, approved prices only
8. Kick-off       14-day live clock starts at kick-off, not at signing
```

Work one stage at a time. Ask for the user's inputs before producing each artifact. Never fill a bracket with a guess.

## Stage guide

| Stage | Inputs to ask for | Output | Reference |
|---|---|---|---|
| Lead list | niche, city/zips, list size, data source available | CSV schema + qualification tiers | `references/lead-list.md` |
| Prospect audit | business name, Google listing / site URL, reviews (pasted or fetched) | Audit brief (client-safe + internal) | `references/prospect-audit.md` |
| Demo brief | audit, logo/photos available, services, hours | Build brief for the demo | `references/demo-build-brief.md` |
| Outreach | owner name, demo link, setter name, sender details | Call plan + email/voicemail sequence | `references/outreach-sequence.md` |
| Demo call + proposal | setter notes from GHL, fit answers | Closer agenda + one-page proposal | `references/demo-call-and-proposal.md` |
| Kick-off | signed client, assets | Onboarding checklist + timeline | `references/onboarding.md` |

## Hand-offs to sibling skills (don't duplicate their scripts)

- Getting past the front desk → `vanguard-gatekeeper`
- First 30 seconds, rapport, booking ask → `vanguard-cold-call-opener`
- "What does it cost?" on the setter call → `vanguard-price-question`
- Role-play, drills, call review for setters → `vanguard-setter-coach`
- Rep KPIs, comp, managing the team → `sales-team-manager`
- Packaging, guarantees, bonuses, offer stack → `hormozi-offer-builder`

## Approved numbers (setters quote only these)

| Item | Line |
|---|---|
| Typical build | "Most of our builds land around two thousand, one-time." |
| Bigger build (booking + gallery) | "Around twenty-six hundred." |
| Care plan | "Optional, about two hundred a month, cancel anytime." |
| Demo | "Free. No card, no contract." |
| Timeline | "Live 14 days after your kick-off call." Never "14 days from today." |
| Discounts, payment plans, terms | Closer only. Setters never guess. |

If the user's agency isn't Vanguard, ask for their price sheet and swap these out. Don't invent prices.

## Truth rules (apply to every artifact)

1. **Every bracket must be verified.** Ratings, review counts, review themes, hours and "no website" all come from the live listing or site, checked that day. If you can't verify it, use the fallback: "no website, just the Google listing."
2. **No invented proof.** No made-up client results, testimonials, case studies or statistics. If the agency has real results, ask the user for them; otherwise leave proof out.
3. **No promised outcomes.** Never "you'll rank #1" or "20 more customers a month." Talk about what the site does (shows up, loads fast on phones, lets people book), not results.
4. **Don't trash anyone.** Not their current site, not Wix, not the nephew, not Facebook.
5. **Audit tone is respectful.** The owner will read it. Frame problems as "costing you customers," never "your site is bad."

## Compliance (non-negotiable)

- Phone: DNC-check every number before dialing. Call 8am–9pm *their* local time. Text only after a clear verbal yes. "Don't call me" means apologize, end the call and add them to DNC the same day.
- Email: real sender name and company, accurate subject line, physical postal address, a plain one-line opt-out honored promptly. Stop the whole sequence on any reply or opt-out.
- Log every touch in GHL the same day, with the setter as Setter Assigned.
- Laws change and vary by state and country. Flag anything borderline as "check current law" rather than asserting it's fine.

## Quality checklist before handing anything over

- [ ] Every fact about the prospect is sourced (listing, site, review quote).
- [ ] The demo link exists and works on a phone.
- [ ] Prices match the approved table or the user's sheet.
- [ ] No guarantees of rankings, traffic or revenue.
- [ ] Email has sender, address and opt-out; call list is DNC-checked.
- [ ] The next step has a specific date/time, not "I'll follow up."

## Sources

Patterns adapted (paraphrased) from public skill repos and the Vanguard setter training. See `references/sources.md`.
