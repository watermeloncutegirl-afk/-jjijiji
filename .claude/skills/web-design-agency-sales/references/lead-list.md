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
