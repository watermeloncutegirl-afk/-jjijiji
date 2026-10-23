---
name: hormozi-offer-builder
description: Builds, audits and objection-proofs sales offers for web design and AI automation agencies using Alex Hormozi's $100M Offers frameworks (value equation, Grand Slam Offer, bonus stacks, guarantees, scarcity, urgency, MAGIC naming, price-to-value). Use when the user asks to "build a grand slam offer", score an offer with the "value equation", "make my offer irresistible", work on "pricing my agency", design a "guarantee" or "bonus stack", name an offer, or stop competing on price. Covers offer design for owners and closers only, not setter call scripts. Every scarcity, urgency or guarantee claim must be real and honoured.
---

# Hormozi Offer Builder (agency edition)

Use this skill to design offers that agency owners and closers sell. The scope is sales offers only, not ads, content or lead generation.

**Core idea (paraphrased from *$100M Offers*):** an offer so good that people feel stupid saying no beats better marketing. If prospects compare you on price, the problem is the offer, not the pitch.

## Who this is for, and who it is not for

- **Owner or closer:** designs the offer, sets prices, guarantees and bonuses, and decides on any discounts or terms.
- **Setter (for example, Vanguard Studios setters):** never improvises offer terms. Setters must not mention specials, "spots left", discounts or payment terms. They use only the approved lines, for example "Most of our builds land around two thousand, one-time" and "I can't set prices or terms. That's [Closer]'s call."
- If the user is a setter, give them the approved lines and point them to the setter training skills. Do not hand them offer levers to use on the phone.

## Ethics guardrails (non-negotiable)

1. **Scarcity must be real.** "3 builds per month" is acceptable only if capacity actually caps at 3.
2. **Urgency must be real.** It has to be tied to a real event, such as a cohort start, a season or a real price change on a real date. No resetting timers and no fake deadlines.
3. **Guarantees must be honoured and easy to claim.** Never guarantee results the agency doesn't control, such as "#1 on Google" or "20 new customers". Guarantee what you control: speed, revisions, responsiveness or uptime.
4. **Bonus values must be defensible.** Use what you would actually charge for the item on its own, or what it costs on the market. Never inflate them.
5. **No invented stats or testimonials.** If proof doesn't exist yet, say so and suggest how to collect it.

When a user proposes something that breaks one of these rules, **flag it explicitly**, explain the risk (trust, refunds, legal or chargebacks) and offer an honest alternative.

## Modes

Ask which mode the user wants if it isn't obvious. Ask one question at a time and work with what they already gave you.

### Mode 1: BUILD (new offer from scratch)
Follow `references/grand-slam-build.md`:
1. **Market check.** Is this a starving crowd? Check for pain, purchasing power, whether they are easy to target, and whether the market is growing. Narrow the niche, for example "towing companies in Ohio" rather than "small businesses".
2. **Dream outcome.** Write it in the customer's own words, such as "my phone rings with jobs", not "SEO-optimized site".
3. **Problems.** List every obstacle, fear and point of friction before, during and after the purchase.
4. **Solutions.** Turn each problem into a named solution ("How do I …?" becomes "The … system").
5. **Delivery vehicles.** Decide how each solution is delivered: done-for-you, done-with-you, DIY, software, templates or support.
6. **Trim and stack.** Keep what is high value and low cost to deliver. Cut what is low value and high cost.
7. **Enhance.** Add bonuses, a guarantee, real scarcity and urgency, and a name. See `references/enhancers.md`.
8. **Price.** Price to value. See `references/pricing.md`.
9. **Output the offer doc** using the template below.

### Mode 2: AUDIT (score and improve an existing offer)
1. Collect the current offer: deliverables, price, terms, guarantee, proof, timeline, and how it is pitched.
2. Score it with the **Value Equation scorecard** in `references/value-equation.md`.
3. Run the **7-point irresistibility check** in the same file.
4. Return the weakest one or two drivers first, each with concrete fixes. Label every fix as **"Suggestion for the owner"**. Never present a fix as a change already made.

### Mode 3: OBJECTION-PROOF (map objections to offer components)
Follow `references/objection-proofing.md`:
1. List the real objections heard on calls. If the user has none, use the agency defaults in that file.
2. Classify each one: price, trust, time, effort, "I already have someone", or authority.
3. Map each one to an offer component that removes it before it comes up: a bonus, a guarantee term, a proof asset, a delivery change or a payment structure.
4. Write a one-line closer response for each, and keep it honest.

## The Value Equation (quick reference)

```
            Dream Outcome  ×  Perceived Likelihood of Achievement
Value  =  ─────────────────────────────────────────────────────────
                  Time Delay  ×  Effort & Sacrifice
```

- Raise the top: a bigger and more specific result, and more belief that it will happen (proof, demos, guarantees).
- Shrink the bottom: faster results, and less work for the buyer (done-for-you work, fewer meetings, nothing to learn).
- The best agency lever is usually **the denominator**. Local business owners pay to avoid doing the work themselves.

## Worked examples

- `references/example-vanguard-web.md`: audit of Vanguard Studios' demo-first web offer (free pre-built demo, about $2,000 build, about $2,600 with booking and gallery, optional care plan of about $200 a month, live 14 days after kick-off).
- `references/example-ai-receptionist.md`: an AI automation agency offer (missed-call text-back and AI receptionist for local service businesses) built from scratch.

## Offer doc output template

```markdown
# [Offer name, MAGIC-built]
**For:** [narrow avatar]   **Dream outcome:** [their words]
## Value equation score: DO _/10 · PL _/10 · TD _/10 (lower is better) · E&S _/10 (lower is better)
## Core deliverable(s)
## Value stack
| Component | Problem it removes | Delivery vehicle | Standalone value (defensible) |
## Bonuses (one per objection)
## Guarantee: [name] [type] [exact terms and how to claim]
## Scarcity / urgency: [what is real, and why]
## Price: [price], [anchor], [payment options]. Value-to-price ratio: _
## Proof we have / proof we need
## What the setter is allowed to say about this offer (approved lines only)
## Flags (anything that is not real, verified or honoured yet)
```

## Reference files
- `references/value-equation.md`: drivers, agency levers, scorecard, 7-point check
- `references/grand-slam-build.md`: the step-by-step build process with prompts
- `references/enhancers.md`: scarcity, urgency, bonuses, guarantee types, MAGIC naming
- `references/pricing.md`: price-to-value, anchoring, why not to compete on price, tiers
- `references/objection-proofing.md`: objection-to-component map for agencies
- `references/sources.md`: credits and sources
