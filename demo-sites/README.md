# Falmouth demo sites

Three demo websites, one folder per business, built from the Falmouth research
pack on 26 October 2026. Each folder holds `index.html` (one file, inline CSS and
JS), `img/` (the business's own photos), `research.md` (sources, what is verified,
what is a placeholder, what to confirm with the owner), `_headers` and `robots.txt`.
`index.html` at the top level is the overview page that links them.

| Folder | Business | Pitch angle | Practical feature |
|---|---|---|---|
| `castle-beach-cafe/` | Castle Beach Café | No website at all | Private evening hire enquiry form |
| `good-vibes-cafe/` | Good Vibes Cafe | Facebook is their website | Full menu with prices, filterable by veggie and vegan |
| `the-front/` | The Front | Dead domain (thefrontfalmouth.co.uk) | Nine handpump beer board and a bring your own food guide |

Stories Tattoo Studio was researched but deliberately not built. The newest
reviews found were one to three years old and no phone, hours or socials were
found, so the studio needs an activity check first.

The copy on all three is written in the first person, as the business's own
site would be, and the credit line in the demo bar and footer reads "by
Scarlett". To use a fuller name, swap it in one pass:

```bash
grep -rl 'by Scarlett' . | xargs sed -i 's/by Scarlett/by Scarlett Cherry Whitthread/g'
```

## Before these go anywhere

1. Add the reviews. Every page carries labelled empty review slots rather than
   invented quotes, because the research pack recorded review themes but not the
   verbatim text for these three. Reviews go in word for word, with the
   reviewer's name and "Google review", 4 and 5 star only.

2. Check the map panel. Each page embeds a Google Maps iframe over a styled
   fallback that shows the address and an "Open in Google Maps" button, so the
   panel still looks deliberate anywhere the frame is blocked.

## Checking them locally

```bash
python3 -m http.server 4400 --directory .
```

Checked at 375px and 1280px: no console errors, no page errors, no horizontal
scroll, every image loads, no tap target under 44px, the open and closed badge
and today's hours row are correct for Europe/London, and each form validates and
then says nothing was sent.

## Deploying

Not deployed. This session has no Netlify CLI and no login. One site per
business, from the parent folder, without linking it:

```bash
N="npx --yes netlify-cli@latest"
(cd /tmp && $N sites:create --name castle-beach-cafe-demo --disable-linking)
$N deploy --site castle-beach-cafe-demo --dir castle-beach-cafe --prod --no-build
```

Every page carries `noindex, nofollow`, an `X-Robots-Tag` header via `_headers`
and a `robots.txt` that disallows everything, so a deployed demo stays out of
search results.
