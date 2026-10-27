# Email to Overton support

Send to **support@overton.io**.
**cc Steffen Böhm** (S.Boehm@exeter.ac.uk) **and your Exeter liaison librarian**
(via libraryhelp@exeter.ac.uk if you don't have a named contact).

**Don't use the live chat widget on overton.io for this.** You need a written answer
you can forward to Steffen with his funding request and keep on file if anyone later
asks what permission the dashboard was built under. Chat gives you neither, and
whoever answers it usually can't speak for the licence terms anyway.

If the email inbox stalls, the better route is sideways rather than back to chat:
**ask your Exeter liaison librarian who Exeter's Overton account manager is.** Every
institutional subscription has a named rep, the library deals with them at renewal,
and a licence-scope question from the account manager's own customer gets a
definitive answer far faster than a support queue. For Q1, Q4 and Q5 below, the
account manager is the correct person — support can only really answer Q2 and Q3.

Why cc them: Overton licences are institutional. The moment they see a named
professor at the subscribing institution on the thread, you stop looking like an
individual asking for developer access and start looking like a contractor doing
sanctioned work. It also shows Steffen you moved the same week he asked — which is
worth as much as the answer.

---

**Subject:** API access query — University of Exeter licence (policy-mentions dashboard)

Hello,

I'm working with Professor Steffen Böhm (Director of Research, Sustainable Futures,
University of Exeter Business School, cc'd) on an internal dashboard showing how
Exeter Management staff appear in the policy documents you index. Exeter holds an
Overton licence and I have premium access on my own account.

Before we scope the project, I'd like to confirm what our licence allows:

1. **API access** — does Exeter's licence include REST API access, and how is a key
   issued? I'd be building on Exeter's behalf rather than for my own use, so if the
   request needs to come from the institution or from Professor Böhm as sponsor,
   please say and I'll arrange it.

2. **Limits** — what are the rate limits, the maximum results per query, and any
   monthly request quota?

3. **Query patterns** — we need two things: (a) retrieving documents that cite a
   given DOI, and (b) full-text search for a researcher's name that returns the
   surrounding text, so we can distinguish a bibliography citation from someone
   being quoted as an expert or authoring the document themselves. Are both
   supported via the API, and does the response include a usable text snippet?

4. **Terms of use** — what do the terms permit for storing retrieved metadata and
   short snippets, and re-displaying them in a dashboard used internally by the
   subscribing institution?

5. **Scale** — phase one covers about 20 staff; a later phase may cover around 250
   (the whole Management department). Would the API suit that, or would the data
   snapshot product be a better fit? If there's a cost difference between them,
   could you outline it so we can budget?

Happy to have a quick call if that's easier.

Many thanks,
Scarlett [surname]
[your email] · [your website]

---

## What each question is actually for

- **Q1** decides whether the 250-staff tier is quotable at a fixed price or at all.
- **Q2** sets the runtime and therefore your day estimate. A 1,000-results-per-query
  cap changes the retrieval design.
- **Q3** is the one most likely to come back as a partial no. If the API returns
  metadata but no text snippet, "mentioned in what way" has to come from the
  document itself, which is slower and changes the quote. Ask it explicitly now
  rather than discovering it mid-build.
- **Q4** is what lets you hand Exeter a stored dataset without a licence problem.
- **Q5** surfaces the snapshot product. For 250 staff a snapshot may be both cheaper
  and faster than hundreds of thousands of API calls — and if there's a cost, it
  belongs in Steffen's funding request, not absorbed by you.

Flag anything that comes back as a "no" to Steffen straight away. A constraint you
report early is a professional judgement; the same constraint found after he's
secured funding is a problem you handed him.
