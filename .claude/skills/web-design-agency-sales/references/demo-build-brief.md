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
