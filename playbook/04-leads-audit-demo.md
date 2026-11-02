# Lead List: Niche + City from Google Maps

## Inputs
- Niche (one per list: "barbershops", not "beauty")
- City or zip codes
- Target size (start with 100–200 per setter per week)
- Data source the user actually has: manual Google Maps, a scraper/API (e.g. a RapidAPI Maps endpoint, Outscraper, Apify), or an existing dataset

Don't scrape in ways that break a provider's terms. If the user has no tool, give a manual research workflow.

## Niches that fit demo-first well
Local, phone-driven, review-heavy businesses where the owner is the decision-maker:
salons and barbers, groomers, trades (roofers, plumbers, HVAC, electricians, landscapers, cleaners), auto repair and towing, restaurants and food trucks, gyms and martial arts, daycares, tattoo shops, detailers.

## CSV schema

```
business_name, category, address, city, phone, website_url, website_status,
facebook_only (y/n), google_rating, review_count, hours, owner_name (if verified),
top_review_theme, notes, tier, dnc_checked (y/n), date_verified
```

`website_status` values: `none`, `facebook_only`, `broken` (doesn't load or SSL error), `not_mobile` (fails a phone check), `outdated` (copyright years old, dead links, no click-to-call), `ok`.

## Qualification tiers

| Tier | Signals | Why |
|---|---|---|
| A | No website or Facebook-only; 20+ reviews; rating 4.0+; open now | Busy, trusted, invisible online. Strongest demo hook |
| B | Broken / non-mobile / outdated site; 10+ reviews | Clear, visible problem the demo fixes |
| C | Decent site but no booking, no click-to-call, or slow on phones | Narrower pitch; lower priority |
| Skip | Permanently closed, franchise/chain (corporate decides), site is `ok`, under 5 reviews with no activity, DNC hit | Won't close or can't be called |

Review count and rating are signals of an active business with word of mouth, not a score of the owner. Note them exactly as shown on the day you checked.

## Verification pass (before a lead goes to a setter)
1. Open the listing: confirm phone, hours, category, rating, review count. Record `date_verified`.
2. Search the business name + city: confirm there's really no site (check Facebook, Yelp and any directory "website" links).
3. If there's a site, open it on a phone (or a mobile emulator): does it load, is the phone number tappable, is there a way to book or get a quote?
4. Read the 10 most recent reviews: write one real theme in their customers' words ("fast", "fair price", "great with kids").
5. Owner name: only if it's in reviews ("Mike was great"), the listing, or the state business registry. Otherwise leave blank; the gatekeeper opener handles it.
6. DNC-check the number. Mark `dnc_checked`.

## Output format
Give the user the CSV (or table), a count per tier, and the 10 A-tier leads to build demos for first. Demos take time, so build in batches sized to what setters can call that week.

# Prospect Audit

Purpose: one short, honest brief that (a) tells the demo builder what to fix and (b) gives the setter and closer one or two true details to use on the phone. Structure adapted from peterhadorn/webdesign-agency-skills `/prospect-audit` (business-language sections, internal technical section kept separate).

## Rules
- **Verified facts only.** Every claim cites where it came from: listing, site URL, or a review quote with the reviewer's first name or date.
- If there's no site, the audit is about the listing and the search experience, not an imagined site.
- No scores the owner could read as an insult. If the user wants a score for internal triage, keep it in the internal section.
- No predicted revenue, traffic or ranking numbers.

## Template

```markdown
# [Business] — Prospect Audit
Checked: [date] · Sources: [Google listing URL], [site URL or "no site found"], [other]

## Summary (one line)
[e.g. "Well-reviewed barbershop (4.8, 212 reviews) with no website. Searchers land on the Google listing only."]

## What's costing you customers
Each item: what a customer experiences → why it loses them. Max 4.
- [e.g. "Searching 'barber near me' on a phone shows the listing, but there's no site to see prices, styles or book. People who want to check first move on to the next result."]
- [e.g. "The Facebook page lists hours that differ from Google (Sat 9–5 vs 9–3)." — only if verified]

## What we'd fix
Outcome-framed, in priority order. Mark quick wins.
1. [A one-page-per-service site that loads fast on phones] (quick win)
2. [Tap-to-call and online booking button above the fold]
3. [Gallery from their own photos, with permission]

## What caught our eye
Genuine positives. This is what the setter uses for rapport.
- "[Real review theme]", e.g. 14 of the last 30 reviews mention "fast"
- [Something specific: years in business on the listing, a strong photo set, a local award they display]

## Hooks for the call (setter/closer only)
- One true detail for the opener: [...]
- Fallback if unsure: "no website, just the Google listing"

## Internal: technical notes (not client-facing)
- Mobile check: [result] · Load: [fast/slow, how checked] · SSL: [ok/error]
- Booking/contact: [none / phone only / form broken]
- Tier: [A/B/C]
```

## Counting review themes
Read the most recent 20–30 reviews. Count only explicit mentions. Report as "X of the last Y reviews mention …", not as percentages of all customers.

# Demo Build Brief

The demo has to exist, work on a phone and look like *their* business before the setter dials. It doesn't have to be the final site. Aim for something a builder can finish in 1–3 hours from a template.

## Asset rules
- Use their real name, phone, address, hours and services from the listing.
- Use their own photos only if they're publicly posted by the business, and note the source; otherwise use neutral stock clearly suitable for the niche and mark it "placeholder" internally.
- Review quotes: copy verbatim with first name/initial and source ("— Dana, Google review"). No editing, no invented testimonials.
- No fake stats ("500+ happy customers") unless the number is on their listing or they said it.
- Put a small "Demo prepared by Vanguard for [Business]" note in the footer and keep it unindexed (noindex, unlisted URL).

## Template

```markdown
# Demo Brief — [Business] ([niche], [city])
Audit: [link] · Tier: [A/B/C] · Builder: [name] · Due: [date, before first dial]

## Goal of the demo
Show the owner how a customer would find, trust and contact/book them on a phone in under 10 seconds.

## Pages (keep it small)
- Home: headline, one-line promise in plain words, tap-to-call, primary CTA
- Services: from the listing/menu, with prices only if publicly posted
- Reviews: 3–5 verbatim quotes
- Gallery: (if real photos exist)
- Contact / Book: map, hours, phone, form or booking embed placeholder

## Copy pulled from them
- Headline idea: built from top review theme, e.g. "[City]'s barbershop for a fast, clean fade"
- Services list: [from listing]
- Hours: [from listing, date checked]
- Quotes: [3–5, with source]

## Primary CTA
[Call now | Book online | Get a free quote] — choose based on how they take customers today.

## Booking
[Their existing tool if any (Square, Booksy, Vagaro) → link it] / [placeholder form] / [none — tap-to-call only]

## Mobile check before handoff
- [ ] Loads on a phone over cellular
- [ ] Phone number is tappable
- [ ] CTA visible without scrolling
- [ ] No lorem ipsum, no other business's name
- [ ] Link works when sent by text and email
```

If the user is building the demo with Claude, recommend the `frontend-design` skill (anthropics/skills) for layout quality.
