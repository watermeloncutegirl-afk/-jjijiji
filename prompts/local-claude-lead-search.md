# Prompt: Local Claude lead search (Penryn & Falmouth businesses without websites)

Paste everything below the line into Claude on your own PC. Use Claude Desktop with **Claude in Chrome** or the built-in browser turned on, or Claude Code with a browser tool. A real browser can open Google Maps, Facebook and Yell properly, and cloud sessions often get blocked on those sites.

Tip: do one town per chat. Penryn first, then start a fresh chat for Falmouth.

---

You are helping me find sales leads. I build websites for small local businesses in Cornwall, UK. I need a list of **real businesses in [TOWN: Penryn (TR10) / Falmouth (TR11)] that do NOT have their own website**.

## How to search

Use the browser and work through these sources in order:

1. **Google Maps.** Search for each category below plus the town name, e.g. "plumber Penryn" or "cafe Falmouth". Open each listing. If the listing has no "Website" button, or only links to Facebook, Instagram or a directory, it's a candidate. Scroll the results to load more listings.
2. **Facebook.** Search for "[category] [town]". Businesses that only have a Facebook page are ideal leads.
3. **Yell.com, Checkatrade, MyBuilder and Bark.** Search each category in the town and look for listings with no website link.
4. **Local directories.** Try Falmouth BID, Penryn town / Penryn Chamber pages, "Love Falmouth", and local Facebook groups like "Falmouth Community" or "Penryn Community". Only read public posts.

Categories to cover: plumbers, electricians, builders, roofers, plasterers, painters & decorators, carpenters, landscapers/gardeners, cleaners, window cleaners, handymen, cafés, takeaways, restaurants, pubs, barbers, hairdressers, beauty/nails, massage/therapists, dog groomers, dog walkers, B&Bs/guest houses, holiday lets, boat/marine services, mechanics/garages, MOT centres, taxis, independent shops, florists, tattoo studios, personal trainers, tutors, photographers.

## How to verify each one (do this for every lead)

1. Google `"<business name>" <town>` and look through the first page of results.
2. Also try `<business name>.co.uk` and `.com` in the address bar.
3. It counts as **no website** if it has only Facebook, Instagram, Google Business Profile, Yell, Checkatrade or similar. A dead or parked domain also counts; note it as "dead site". So does a one-page directory profile.
4. If you find a working site on their own domain, skip the business. If you're unsure, include it with Low confidence.

Confidence levels:
- **High:** properly searched and no site found.
- **Medium:** probably no site.
- **Low:** unsure.

## Rules

- Only include **real businesses you actually saw**. Never invent names, phone numbers or reviews.
- Only collect **publicly listed business** contact details. Don't collect private individuals' personal info.
- Don't message, call, or sign up to anything. Only read and search.
- If a site asks you to log in or hits a CAPTCHA, skip it and move on. Tell me which sites you couldn't access.
- Go for volume: aim for **30+ leads for Penryn** and **50+ for Falmouth**.

## Output

Save the results as a CSV file named `leads-<town>.csv` with exactly these columns:

```
name,category,town,address,phone,online_presence,google_reviews,evidence_url,confidence,sales_angle
```

- `online_presence`: what they DO have, e.g. "Facebook (2.1k likes), Google 4.7★".
- `google_reviews`: the number of Google reviews, or blank.
- `sales_angle`: one line on why they need a site. Example: "120 Google reviews, busy summer café, no online menu — tourists can't find opening hours."

After the CSV, give me a short summary:
1. The total number of leads and the count per category.
2. Your **top 10 hottest prospects**, ranked. Busy businesses with lots of reviews and no site rank highest, and so do trades paying for Checkatrade.
3. Which sources were blocked or didn't work.
4. Any leads you were unsure about.
