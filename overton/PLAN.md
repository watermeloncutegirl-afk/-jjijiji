# Overton mentions dashboard — analysis & build plan

Source: Steffen Böhm (Professor in Organisation & Sustainability, Director of Research
for Sustainable Futures, University of Exeter Business School), four emails on
Fri 23 Oct 2026.

---

## 1. What he actually asked for

Four separate asks arrived in one thread. Only one is a build; the rest are sales
and advice. Keep them separate — they have different clients, budgets and timelines.

| # | Ask | Type | Decision needed from him |
|---|-----|------|--------------------------|
| A | **Overton mentions dashboard** — trial for Böhm + Pascucci, then quote for 20 staff and for 250 staff | Build + quote | Funding, which tier |
| B | Large-scale grey-literature analysis ("thousands of documents") | Future project, scoped separately | Research question first |
| C | Advice on *your* site/CV (testimonials, logos, case studies, cut to ≤6 distinct tools) | Action for you, no deliverable to him | — |
| D | **steffenboehm.net** redesign + migration off Wix (£24/mo) + new content from his papers | Build + quote | Quote approval |

His stated decision path on A is explicit: *"send me a little proposal / quote and,
based on that, I can then see what that's something I want to go for and can get
funding for."* So the trial is not the product — the trial is the thing that makes
the quote credible. Build the trial to be convincing, not complete.

Two details in his email are the real test, and both are easy to miss:

1. **"I only came up using the German spelling of my name."** He is telling you his
   own search undercounted him. Böhm / Boehm / Bohm are three different queries. If
   your dashboard shows one number he can't check, it's worthless to him; if it shows
   *the variants it searched and what each returned*, it's immediately trustworthy.
2. **"which academic colleagues is mentioned in what way"** and *"more finegrained
   data on the type of mentions in which publications"*. He wants the **kind** of
   mention, not just the count. Being cited in a bibliography, being quoted as an
   expert, and authoring the policy document yourself are three different impact
   stories, and only the third one gets him anywhere with a REF panel.

Stefano Pascucci is the control case: an unaccented, common Italian surname. Böhm
tests name variants, Pascucci tests false positives. Reporting both honestly —
including *"N of these are probably a different Pascucci"* — is the differentiator.

---

## 2. Blockers to clear before any code runs

### 2.1 Does Exeter's licence include API access? (step zero)
Overton has a REST API and a bulk "data snapshot" product, but they are **not
automatically part of a reading-room licence**. Overton's own help centre lists
"API and data snapshot access" as a separate topic, and the institutions that
advertise API access describe it as an *expanded* subscription. Exeter's library
guide doesn't mention the API at all.

**Action (yours, day 1):** create the Exeter account he asked for, then email
support@overton.io (cc your Exeter liaison librarian) asking three questions:
- does the Exeter licence include REST API access, and how is a key issued?
- what are the rate limits and result caps per query?
- what do the terms permit for storing and re-displaying retrieved metadata and
  snippets in an internal dashboard for the subscribing institution?

This single answer sets the price and feasibility of the 250-staff tier. Don't quote
tier 2 as a firm fixed price until it comes back.

### 2.2 The fallback, and the line you don't cross
- **With API:** 2, 20 and 250 staff are the same pipeline with a bigger input file.
- **Without API:** manual UI exports (Overton exports Excel/CSV/RIS). Fine for 2 and
  tolerable for 20. For 250 it becomes hundreds of hand-run searches — quote it as
  time-and-materials or decline the tier until API access exists.
- **Do not scrape the authenticated UI.** It is very likely a licence breach, the
  client *is* the licensee, and a university research director cannot accept a
  deliverable built that way. Say this in the proposal as a professional constraint;
  it reads as competence, not as a limitation.

### 2.3 Data protection — one paragraph in the proposal, not a footnote
Compiling named mention-profiles for 250 identified staff is personal-data
processing. Exeter is the controller; you are a processor and need a short data
processing agreement. Practically: deliver it as *research visibility*, aggregate
first, individual drill-down second, and let the department decide on circulation.
Flag the league-table risk once and let him own it — a Director of Research knows his
own politics better than you do. Raising it unprompted is what makes the quote look
like it came from a professional.

### 2.4 What I need from you to build the trial
I can't reach Overton from here — it's behind Exeter SSO. To build the working trial
I need either an API key in an env var, or, for the manual route, these exports saved
into `overton/data/raw/`:
- citation search for each of: `Böhm`, `Boehm`, `Bohm`, `Pascucci` (CSV/Excel export)
- full-text search for the same four strings
- if available, each person's Overton author/profile page export

---

## 3. "Can you build an AI model for this?" — the honest answer

He asked whether you can build an AI model to analyse the Overton database. Answer
precisely, because over-claiming here is the fastest way to lose an academic client:

> Nothing here needs a model to be *trained*. The hard parts are identity resolution
> (which "Boehm" is this?) and classifying how a person is mentioned. That's a
> retrieval pipeline plus a language model used as a classifier over retrieved text,
> with every number traceable back to a source document. It's more reliable than a
> trained model and you can audit it.

Say that in the proposal in roughly those words. It also pre-empts the obvious
question from a sceptical colleague: *where does this number come from?*

---

## 4. Pipeline design

```
overton/
  config/
    roster.csv              # staff_id, display_name, orcid, dept, group, manual_variants
  src/
    01_resolve_identities.py
    02_fetch_overton.py
    03_normalise.py
    04_classify_mentions.py
    05_build_outputs.py
  data/
    raw/                    # every API response / UI export, verbatim, hashed filename
    interim/
    identities.json
    mentions.csv
    documents.csv
  outputs/
    overton_dashboard.html  # single self-contained file
    overton_mentions.xlsx
  README.md
```

Boring, file-based, re-runnable. No database, no server. Every stage reads files and
writes files, so any number in the dashboard can be traced back to a raw response.

### Stage 1 — identity resolution (`01_resolve_identities.py`)
The fix for the Böhm problem. For each roster row:
- Look the person up in **OpenAlex** by ORCID (free, no key, generous limits). This
  returns their full publication list with DOIs *and* every author-name spelling that
  appears in print — so variants are **discovered from data, not guessed**. Böhm /
  Boehm / Bohm / S. Böhm all surface automatically.
- Add transliteration variants programmatically (ö→oe, ö→o, strip accents) and merge
  with any `manual_variants` from the roster.
- Record affiliation tokens ("Exeter", "Penryn", "University of Exeter Business
  School") and top concepts/topics — these are the disambiguation evidence in stage 4.

Output: `identities.json` — one record per person with `dois[]`, `name_variants[]`,
`affiliations[]`, `topics[]`.

### Stage 2 — retrieval (`02_fetch_overton.py`)
Two query families per person, because they answer different questions:
- **Citation mentions:** query by DOI for each of their publications. High precision —
  a DOI match is not ambiguous. This is "my research reached policy".
- **Text mentions:** full-text query per name variant. Lower precision, needs stage 4.
  This is "I am named in a policy document".

Cache every response to `data/raw/<sha1-of-query>.json` and never re-request a cached
query. Re-runs then cost nothing, the pipeline is reproducible, and if Overton's index
changes you can diff it. Respect rate limits with simple backoff; log every query to a
manifest so you can show the client exactly what was searched.

### Stage 3 — normalise (`03_normalise.py`)
Two tidy tables:
- `documents.csv` — `doc_id, title, publisher, publisher_type, country, doc_date, url, doi`
- `mentions.csv` — one row per **(staff_id, doc_id, mention_type)** with `snippet`,
  `matched_variant`, `source_query`, `confidence`

One row per mention-in-a-document, not per person, so every aggregate in the dashboard
is a simple group-by and the counts can't drift between views.

### Stage 4 — classification & confidence (`04_classify_mentions.py`)
This is the stage that answers *"mentioned in what way"*.

**Mention type** — rule-based where possible, LLM where not:
- `cited_work` — matched via DOI in the document's references
- `authored_policy_doc` — the person is an author of the policy document itself (the
  strongest impact signal; surface it prominently)
- `expert_quoted` / `named_in_text` / `committee_or_acknowledgement` / `passing_reference`
  — classified by a Claude call over the snippet, with a strict JSON schema, batched,
  cached by snippet hash

**Confidence tier** — the part that earns trust:
- `confirmed` — DOI match, or name match plus an affiliation token or a co-occurring
  citation in the same document
- `probable` — name variant plus topic overlap with the person's research
- `unverified` — bare name match only (common surnames: Pascucci, Bohm)

Show the tiers in the UI as separate counts and let him filter. **Never collapse them
into one headline number.** A Director of Research who can see your uncertainty will
trust the rest of your numbers; one who catches an inflated count won't.

### Stage 5 — outputs (`05_build_outputs.py`)
Both formats he asked about, from the same tables, so they can never disagree.

**Excel** (`overton_mentions.xlsx`): summary sheet (one row per person, counts by type
and tier), a full mentions sheet (filterable), a documents sheet, and a methods sheet
naming the variants searched and the date of the run. Academics want the underlying
rows; give them the rows.

**HTML dashboard** (`overton_dashboard.html`): one self-contained file with the JSON
embedded — no backend, no hosting bill, works from an email attachment, and still
works in three years. At this scale (250 staff × a few hundred mentions is single-digit
MB) client-side filtering is instant. Host on Cloudflare Pages or GitHub Pages free
behind a password if he wants a link instead of a file.

---

## 5. Dashboard design

### Trial view (2 people — build this first)
He asked *"how would a dashboard for these two SF members look?"*, so lead with the
comparison:
1. **Two cards side by side** — Böhm and Pascucci: total mentions, split by type,
   confidence mix, date range, number of distinct publishing bodies.
2. **Name-variant panel** — a small table: variant searched → documents found. This is
   his own warning, answered visibly. Expect it to be the thing he remarks on.
3. **Timeline** — mentions per year, two series.
4. **Breakdowns** — publishing body, country, document type (IGO / national govt /
   think tank / NGO).
5. **Document table** — every mention: document title (linked to Overton), publisher,
   date, mention type, confidence, and the snippet showing *how* they're named.
6. **Methods note** — what was searched, when, what the tiers mean.

### Full view (20 / 250 staff)
Same data model, one layer up:
- **Roster table** — sortable, searchable, grouped by research group or department;
  counts by mention type; sparkline per person
- **Click through to the single-person view** above
- **Department rollups** — total policy reach, top publishing bodies citing Exeter
  Management, country spread, year trend
- **Filters** — year, country, publisher type, mention type, confidence tier
- **CSV export** of any filtered view
- **Coverage/caveats panel** — staff with no ORCID, unresolved identities, variants not
  yet checked. Visible gaps beat silent ones.

At 250 staff, add a **review queue**: the `unverified` mentions ranked by how much they
would change someone's count, so a research administrator can confirm or reject in bulk
later. Precision at 250 names is a human-in-the-loop problem, and pricing a few hours
of review is more honest than pretending the classifier is perfect.

---

## 6. Build sequence

| Step | Work | Depends on |
|------|------|-----------|
| 0 | Exeter Overton account; email support re API, limits, terms | — |
| 1 | Roster for the 2 trial names; ORCIDs; OpenAlex identity resolution | — |
| 2 | Retrieval: API if keyed, else your manual exports into `data/raw/` | 0 |
| 3 | Normalise to `mentions.csv` / `documents.csv` | 2 |
| 4 | Classification + confidence tiers | 3 |
| 5 | Excel + HTML trial dashboard, Böhm vs Pascucci | 4 |
| 6 | Proposal/quote (tiers below), sent with the trial | 5 |
| 7 | On approval: scale roster to 20, then 250; add review queue | 6 |

Steps 1 and 3–5 I can build now. Step 2 is the only hard dependency on you.

---

## 7. Quote scaffold

Numbers to adjust to your own rates — the *structure* is what matters, because it
lets him pick a tier and find funding for it.

**A. Overton dashboard**
- **Trial (2 staff): £0, included.** Say so explicitly. It's your portfolio case
  study and it costs you a day.
- **Tier 1 — 20 staff (Sustainable Futures): ~£1,200–£1,800** one-off. Identity
  resolution, retrieval, classified mentions, Excel + hosted dashboard, methods note,
  one refresh inside 3 months.
- **Tier 2 — 250 staff (whole Management dept): ~£3,500–£6,000**, conditional on API
  access. Everything above plus department rollups, the review queue, and a handover
  doc so the department can re-run it. Without API access, quote as a day rate with a
  capped estimate and say why.
- **Refresh: ~£400–£800 per quarterly run**, or an annual agreement. Policy documents
  keep appearing; a one-off dashboard is stale within months — and recurring revenue
  is worth more to you than the build fee.
- **Add-on — grey-literature analysis (his ask B):** quote separately after he states
  a research question. "Download and review thousands of documents" is a research
  project, not a dashboard feature, and it may need Overton's data-snapshot product.

**B. steffenboehm.net redesign (his ask D)**
- He pays Wix ~£24/mo = **~£288/yr**. Lead with that number.
- **Design + build + migration + content distillation: ~£900–£1,500** one-off.
- Static site (Astro or Eleventy), markdown content, deployed to Cloudflare Pages or
  Netlify — **£0 hosting**, domain ~£15/yr. He saves ~£270/yr and leaves Wix, which he
  said he wants to do on principle.
- Content: you distil his papers into an expertise/projects overview. Cap the rounds
  (two rounds of revisions) or this is where the project overruns.
- Optional care plan £10–20/mo for updates, or hand him a markdown workflow so he can
  edit publications himself. Academics add publications constantly; he'll want this.
- Keep this quote in its own email. Two quotes in one message halves the chance either
  gets approved.

---

## 8. Closing the loop on his advice about your site (ask C)

His feedback and this project fit together, so act on them at once:
- The Overton dashboard **is** the portfolio case study he said you were missing —
  real client, real problem, screenshots, a stated outcome.
- When the trial lands well, ask him for two things in the same email: **permission to
  use the University of Exeter logo**, and **a two-line testimonial**. He already
  volunteered that you should have both; asking right after you deliver something he
  likes is the moment with the highest chance of a yes.
- Cut the tool list to ≤6 distinct tools (his word was "bewildering" at 10+). A
  "policy-impact / research-visibility dashboard" is now one genuinely distinct tool
  with a named client behind it — exactly the distinctness he said was missing.

---

## 9. Findings from the live stage-1 run (27 Oct 2026)

Stage 1 doesn't touch Overton, so it ran today against the **ORCID public API**,
which needs no key and no authentication. Both trial identities resolved, and the
results change three things in the plan above.

### Böhm — the variant problem is already solved, from his own record
ORCID **0000-0002-0888-1362**. His ORCID record declares the other-name forms
**"Steffen Bohm"** and **"Steffen Boehm"** himself. So the three spellings he warned
you about come from authoritative data, not from guesswork — the variant panel in the
dashboard can cite its source. 97 declared works, 77 with DOIs, 2003–2026.

**Change to the plan:** his career spans **Exeter, Essex, Lancaster and Warwick**.
Stage 4 disambiguation must accept all four affiliation tokens. Scoring on "Exeter"
alone would push his pre-2015 policy mentions into `unverified` and undercount him —
the exact failure he already complained about, in a new form.

### Pascucci — a coverage problem the dashboard has to disclose
ORCID **0000-0001-5925-9496**, but the record lists only **10 works** (2017–2026)
against a real output that is plainly much larger, and declares no name variants.
DOI-based citation matching would therefore undercount him severely, and for the
worst possible reason: not because his research has less policy reach, but because
his ORCID is sparse.

This is the single most useful thing to show Steffen. It means **dashboard quality
depends on ORCID hygiene**, which hands him a concrete lever he controls: ask SF
staff to populate their ORCID records. Build it into the product as a **"data
readiness" column** per person (ORCID present / works declared / variants declared),
and into the quote as a **data-readiness audit** line item for the 20- and 250-staff
tiers. It turns an awkward caveat into something he can act on.

**Change to the plan:** ORCID alone is not a sufficient publication source. Stage 1
needs a fuller list keyed by ORCID, then the union of both.

### Publication-source options, tested today
- **ORCID public API** — works unauthenticated, reliable, but only as complete as the
  researcher chose to make it. Good for variants and identity, not for full output.
- **Crossref** — free and keyless, but `query.author` is a loose text match, not an
  author identifier: "Stefano Pascucci" returned 231,189 results. Unusable as a
  publication list without an ORCID filter. Also rate-limited on a shared IP.
- **OpenAlex** — the right source, since it resolves by ORCID and returns both the
  full DOI list and every name spelling in print. Its free tier is exhausted on this
  container's shared IP, so it needs a free API key. **Getting one means submitting
  your email address to OpenAlex** — your call, and I won't do it without you saying so.

### Overton API — host confirmed, access not
`api.overton.io` resolves (51.178.75.50) but refuses unauthenticated connections at
the connection level rather than returning an HTTP error, so the endpoint shape, auth
header and limits can't be confirmed without a key. Nothing to infer from that either
way — it's just why the questions in `overton-support-email.md` have to be asked
rather than discovered.
