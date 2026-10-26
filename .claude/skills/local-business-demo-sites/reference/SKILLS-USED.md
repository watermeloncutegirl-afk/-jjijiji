# Skills and tools used to build the demo sites

## Skills actually loaded during the demo builds
| Skill | Where it came from | What it was used for |
|---|---|---|
| `web-design-agency-sales` | Anthropic skills plugin (claude.ai) | The demo-first pipeline, truth rules (verified facts only, no invented proof, no promised outcomes, don't trash anyone), audit and demo brief structure, need-based lead tiers. |
| `animate` | ~/.claude/skills | Loaded earlier in the session for the AI tools site's motion; the same restraint (subtle, reduced-motion aware) carried into the demos. |

## Skills whose guidance I applied (installed, recommended to load explicitly next time)
| Skill | Why it matters for these sites |
|---|---|
| `frontend-design` | Distinctive, non-template look per business: brand-derived fonts, colours, one signature motif. |
| `design-taste-frontend` / `impeccable` | Avoiding generic "AI website" aesthetics; spacing and type polish. |
| `form-design` | Quote/booking/enquiry forms: labels, validation, sensible inputs (plate field, weekday-only dates). |
| `wcag-accessibility-audit` | Contrast, 44px tap targets, reduced motion, alt text. |
| `marketingskills-copywriting` / `marketingskills-copy-editing` | Short, plain copy in the owner's voice built from reviews and bios. |
| `ux-psychology` / `fitts-law` / `hicks-law` / `jakobs-law` | One main CTA, sticky call bar on phones, familiar layout order. |
| `visual-hierarchy` | Hero, rating badge and open-now status read first. |
| `vanguard-client-delivery` | What happens after the owner says yes (your build SOP). |
| `built-in-browser` (plugin) | Researching Google Maps, Facebook and Instagram in the in-app browser. |

## Sibling sales skills (for after the demo is live)
`vanguard-cold-call-opener`, `vanguard-gatekeeper`, `vanguard-price-question`, `vanguard-setter-coach`, `hormozi-offer-builder`.

## Non-skill tools in the workflow
- **In-app browser** (Claude desktop): Google Maps, Facebook, Instagram, Gas Safe Register, checking whether a website exists.
- **JavaScript in the page**: pulling hours, reviews, phone, website link and "By owner" photo URLs out of Google Maps.
- **curl + Python Pillow**: downloading photos, fixing rotation, resizing, compressing, contact sheets.
- **python3 http.server + preview tool**: local checks at phone and desktop widths.
- **Netlify CLI** (`npx netlify-cli`): one site per business, created with `--disable-linking`.

## New skill made from this workflow
`local-business-demo-sites/SKILL.md` (in this folder, and installed at `~/.claude/skills/local-business-demo-sites/`). It contains the whole workflow, the rules, code snippets and an example site in `templates/`.
