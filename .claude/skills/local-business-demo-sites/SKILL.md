---
name: local-business-demo-sites
description: Research a local business with no website (Google Maps, Facebook, Instagram), then build a practical, honest, mobile-first demo website using their own photos, branding, hours and verbatim reviews, and publish it to its own Netlify URL as a clearly labelled, noindexed demo. Use when the user pastes one or more local businesses (name, category, street, review count, "nothing at all" / "Facebook as website") and wants demo sites to pitch them.
---

# Local Business Demo Sites

Demo-first web design sales: the demo exists before anyone contacts the owner, so "we already built you a demo" is true. Every fact on the page is verified that day. Nothing is invented.

## Hard rules (never break)

1. **If the business already has a real, working website, do not build.** Report it and skip. Exceptions worth flagging as warm leads, not skips: a dead domain (e.g. Wix "ConnectYourDomain" error), a "Coming soon" placeholder, or a Facebook/Instagram/link-in-bio page used as the website.
2. **No invented facts.** No prices (use a visible "PRICE TO ADD" slot), no stats, no testimonials, no awards, no years in business, no staff names unless they appear in reviews or the business's own posts, no "parking available", no locations or claims you did not see.
3. **Reviews are verbatim.** Copy the exact text, first name or display name as shown, labelled "Google review". Never edit wording, never combine, never use 1 to 3 star reviews.
4. **Their photos only.** Use photos the business posted ("By owner" on Google Maps, their Facebook/Instagram). Never stock photos presented as theirs. Customer photos only if clearly of the place, and prefer owner ones. If there are no photos, use clearly labelled placeholder slots ("Shopfront photo to add").
5. **No home addresses.** If the address looks residential (sole trader, house number on a residential road), show only "Based in [Town]" and the service area if verified.
6. **It must be obviously a demo.**
   - Black bar at the top: "Demo preview prepared for [Business] by [Your name] · Not the official website".
   - Footer line: "Demo website prepared for [Business] by [Your name]. Not the official site."
   - `<meta name="robots" content="noindex, nofollow">`, a `_headers` file with `X-Robots-Tag: noindex, nofollow`, and `robots.txt` with `Disallow: /`.
7. **Forms never send.** Validate, then show: "This is a demo, so nothing was sent. On the live site, your [request] goes straight to [Business]..."
8. **Check identity.** Make sure the Facebook/Instagram you found is the same business (same town, same address or phone). Same-name businesses elsewhere are common. If the social link now points to a different business, or the newest review is years old, pause and ask the user before building.
9. **Writing style:** UK English. Never use em dashes. Plain, warm, specific copy in the business's own voice, built from their bio, posts and review themes.
10. **Record conflicts, don't resolve them by guessing.** If Google and Facebook hours differ, use the most recent source on the page and log "OWNER TO CONFIRM" in research.md.

## Workflow

### 0. Intake
For each pasted business capture: name, category, street/town, review count and rating, and the "website" note. Work through them one at a time, finishing and deploying each before the next. If the user asks to "filter by need", rank first (see Need filter below) before building.

### 1. Research (in-app browser first, Chrome extension only as fallback)
Open Google Maps: `https://www.google.com/maps/search/<name>+<street>+<town>`. Keep the viewport at desktop size (mobile layout breaks scraping).

Collect with JavaScript in the page:
- Website link: `document.querySelector('a[data-item-id="authority"]')?.href`
- Phone: `[data-item-id^="phone"]` text
- Address: `[data-item-id="address"]` text
- Hours: rows of the hours `table tr` (click the hours dropdown first)
- Rating, review count, category, price band, attributes (dine-in, LGBTQ+ friendly, etc.)
- Reviews: open the Reviews tab, sort by Newest, click every `button.w8nwRe` ("More") to expand, then read each `[data-review-id]`: name `.d4r55`, text `.wiI7pd`, date `.rsqaWe`, stars from the aria-label. Note the newest review date (an activity check).
- Owner photos: open Photos, click the tab whose aria-label or text is "By owner", scroll the photo panel to load more, collect `img` src values containing `googleusercontent` and `gps-cs-s`, strip the size suffix and request `=w1400-h1400`.

Then check:
- The website link, if any: is it live and theirs? (see Hard rule 1)
- Facebook page: bio, followers, hours, About, phone, email, recent posts, photos (signed `scontent` URLs expire, so download them straight away).
- Instagram: bio text and handles (read the main `innerText`).
- Trade registers where relevant (e.g. Gas Safe Register for gas engineers, quote the registration number only if it matches).
- Any flyers, menus or price lists in their photos (these are first-party facts you can quote).

Download images into `<slug>/img/` with curl, then process with Python PIL:
```python
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
im.thumbnail((1400,1400)); im.save(dst, 'JPEG', quality=76, optimize=True, progressive=True)
```
Make a contact sheet in the scratchpad and look at it, so you know which image is the shopfront, interior, product, team, etc. Name files by content (`shopfront.jpg`, `interior.jpg`) not number, so you can't mislabel them.

### 2. Write research.md (in the site folder)
```
# [Business] (checked [date]: [sources])
- Address, phone, rating + count (newest review date), website status.
- Hours (source).
- Their own words (bio/tagline/flyer quotes).
- People named in reviews.
- Review themes (what customers keep praising).
- Photos: where they came from; anything NOT used and why.
- OWNER TO CONFIRM: prices, conflicting hours, staff still there, booking destination, anything inferred.
```

### 3. Plan the site from the business type
Pick the one job the site must do for a customer on a phone, and make that the primary CTA:
- Barber / salon / nails: walk-ins vs appointments, services, "call to book", team.
- Café / pub / restaurant: open now, menu highlights from photos/posts, where we are, what people love.
- Trades (plumber, landscaper, builder): call now, quote request form (job type, postcode, photos optional), registrations, service area, before/after.
- Garage / MOT: book MOT form (registration plate input, weekday-only dates), GOV.UK MOT history link, reminder opt-in.
- Tattoo studio: artists and styles, portfolio, enquiry form (placement, size, idea), aftercare.
- Pet groomer: services, first groom / nervous dogs reassurance, booking request.
Then one practical feature that solves a real problem the reviews or listing reveal (e.g. "When's your MOT due?" quick form, loyalty card display, before/after slider, open-now badge).

### 4. Design direction
Derive it from their branding: logo colours, shopfront sign, Facebook cover, van livery, flyers. Give every site a distinct personality, never a reused template look:
- Choose 1 display font + 1 body font from Google Fonts that match the brand's feel (e.g. Alfa Slab One + Barlow for a classic barber, Saira Condensed + Inter for a garage, Roboto Slab + Nunito for a friendly groomer).
- Define colours as CSS custom properties in `:root`. Check text contrast meets WCAG AA.
- One signature visual motif from their world (barber pole stripes, checkerboard, number plate, tattoo flash poster, gold geometric lines).
- Motion is subtle and respects `prefers-reduced-motion`.

### 5. Build (single static page)
`<slug>/index.html` with inline CSS and JS, plus `img/`, `_headers`, `robots.txt`, `research.md`. Mobile-first. Required sections, in this order unless the business type suggests otherwise:
1. Demo bar.
2. Header: name/logo + primary CTA button (call or book). On phones hide the subtitle, keep the name on one line, CTA at least 44px tall.
3. Hero: their best photo, a one-line promise in their own voice, rating badge ("4.9 from 89 Google reviews"), live open/closed status.
4. Services / what they do (only verified items; "PRICE TO ADD" where a price would go).
5. Gallery of their photos (lightbox with `<dialog>` is nice).
6. Reviews: 3 to 6 verbatim, name + "Google review".
7. Practical feature / form (demo mode).
8. Hours table with today's row highlighted, address, Google Maps embed `https://www.google.com/maps?q=<encoded address>&output=embed`, directions link `https://www.google.com/maps/dir/?api=1&destination=<encoded address>`.
9. Footer with demo line, social links that you verified.
10. Sticky mobile call bar (Call + primary action) at the bottom on small screens.

Open/closed status (Europe/London), HOURS in minutes from midnight, Monday first, null = closed:
```js
const HOURS=[[480,1020],[480,1020],[480,1020],[480,1020],[480,1020],null,null];
const fmt=m=>{const h=Math.floor(m/60),mm=m%60,ap=h>=12?'pm':'am',h12=((h+11)%12)+1;return h12+(mm?':'+String(mm).padStart(2,'0'):'')+ap};
const p=Object.fromEntries(new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/London',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()).map(x=>[x.type,x.value]));
const day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(p.weekday), now=(+p.hour%24)*60+(+p.minute), h=HOURS[day];
const el=document.getElementById('status'),t=el.querySelector('span');
if(h&&now>=h[0]&&now<h[1]){el.classList.add('open');t.textContent='Open now until '+fmt(h[1]);}
else{let d=day,n=0;do{d=(d+1)%7;n++;}while(!HOURS[d]&&n<7);t.textContent=(h&&now<h[0])?'Opens today at '+fmt(h[0]):'Closed · opens '+(n===1?'tomorrow':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][d])+' at '+fmt(HOURS[d][0]);}
document.querySelectorAll('#hours tr')[day]?.classList.add('today');
```
If the business has no listed hours, leave out the status badge and say "Hours to add".

Demo form handler:
```js
f.addEventListener('submit',e=>{e.preventDefault();if(!f.reportValidity())return;done.style.display='block';f.querySelector('button[type=submit]').disabled=true;});
```

`_headers`:
```
/*
  X-Robots-Tag: noindex, nofollow
```
`robots.txt`:
```
User-agent: *
Disallow: /
```

### 6. Verify locally
Serve the parent folder (e.g. `python3 -m http.server 4400 --directory ~/demo-sites`) through the preview tool and check:
- Console has no errors, every image returns 200 (`curl -s -o /dev/null -w "%{http_code}"`).
- Phone width (375px): no horizontal scroll, header doesn't wrap, call bar visible, tap targets 44px.
- Desktop width looks deliberate, not stretched.
- Open status and today's hours row are right.
- Form validates and shows the demo message.
- Re-read every sentence against research.md. Delete any claim you can't point to a source for. Search the file for em dashes and remove them.

### 7. Deploy to Netlify (one site per business, never link the folder)
```bash
cd ~/demo-sites && rm -rf .netlify
N="npx --yes netlify-cli@latest"
(cd /tmp && $N sites:create --name <slug>-demo --disable-linking)
$N deploy --site <slug>-demo --dir <slug> --prod --no-build
rm -rf .netlify
```
Then `curl` the live URL and an image to confirm 200s. (Linking the shared folder makes later deploys overwrite the first site, which is why linking is disabled.)

If the user will open the HTML file directly from disk, also produce `<slug>-standalone.html` with images embedded as base64 so nothing breaks.

### 8. Update the overview and report
Add `<li><a href="<slug>/">[Business] <span>[one-line description]</span></a></li>` to the overview `index.html` before `</ul>`.

Report to the user, per business:
- Live URL.
- What the site does (the practical feature).
- What's verified vs placeholder.
- OWNER TO CONFIRM list.
- Pitch angle (e.g. "dead Wix domain", "Facebook is their website", "MOT form replaces phone tag").
Skipped businesses: say why (has a website, identity unclear, closed).

## Need filter (when asked to rank leads)
- **Tier 1:** no website at all, active (recent reviews), service business where calls/bookings/quotes matter (trades, garages, salons), or a dead/placeholder domain.
- **Tier 2:** Facebook or link-in-bio as the website, still active; hospitality with lots of reviews but no menu/hours page.
- **Tier 3:** very few reviews, inactive for 1+ years, chains/franchises, or already has a decent site.

## Before handing over (checklist)
- [ ] Had no real website (or dead/placeholder, flagged).
- [ ] Identity of socials confirmed.
- [ ] Every fact traceable to research.md; reviews verbatim with names.
- [ ] No invented prices, stats, staff, amenities or years.
- [ ] Only their photos (or labelled slots); no home address.
- [ ] Demo bar, footer line, noindex meta, `_headers`, `robots.txt`.
- [ ] Forms in demo mode.
- [ ] Mobile checked at 375px; no console errors; images 200.
- [ ] No em dashes.
- [ ] Deployed to its own Netlify site and live URL checked.
