---
name: ai-automation-agency-sales
description: Sells and scopes AI automations for local businesses (missed-call text-back, AI receptionist or voice agent, review requests, lead follow-up, booking automation). Covers offer selection by fit signals, an ROI-based discovery call with a calculator built only from the prospect's own numbers, demo-first outreach (a recorded or live demo of an agent using their business info), setup plus retainer and pilot pricing, a proposal template, delivery handoff to n8n or Vapi/Retell, and compliance risk notes. Use when the user mentions an "AI automation agency", "AAA", "sell AI agents", "voice agent", "AI receptionist", "missed call text back", "ROI calculator", "discovery call for automation", "automation proposal", "retainer pricing" or "pilot offer".
---

# AI Automation Agency Sales

Sell one clear automation that fixes a leak the owner already feels, prove it with a demo built on their business, price it with numbers they gave you, then hand off cleanly to delivery.

## Pipeline

```
1. Pick the offer   match fit signals to one automation (not a menu of 10)
2. Outreach         demo-first: record a 2–3 min demo using their real business info
3. Discovery call   ROI questions → calculator with THEIR inputs
4. Price            setup + monthly, or a paid pilot
5. Proposal         one to two pages
6. Handoff          build spec for n8n / Vapi / Retell; compliance checks
```

| Stage | Reference |
|---|---|
| Offer menu + fit signals | `references/offers.md` |
| Discovery script + ROI calculator | `references/discovery-roi.md` |
| Demo-first outreach | `references/demo-first.md` |
| Pricing structures + proposal template | `references/pricing-proposal.md` |
| Delivery handoff | `references/delivery-handoff.md` |
| Compliance and risk | `references/compliance-risk.md` |
| Credits | `references/sources.md` |

## Sibling skills (reuse, don't duplicate)

- Cold-call scripts: `vanguard-gatekeeper`, `vanguard-cold-call-opener`, `vanguard-price-question` (adapt "we built a demo website" → "we built a demo of an AI receptionist for [Business]")
- Role-play and call review: `vanguard-setter-coach`
- Team KPIs and comp: `sales-team-manager`
- Offer stacking, guarantees, naming: `hormozi-offer-builder`
- Selling a website alongside the automation: `web-design-agency-sales`

## Honesty rules (hard)

1. **No invented numbers.** Never state industry stats, "businesses miss 62% of calls," or past client results unless the user provides a real, sourced figure. The ROI calculator uses only the prospect's answers; every assumption is labelled and agreed with the prospect.
2. **No guaranteed results.** "Recovers missed calls automatically" describes what it does. "Will make you $10k a month" is a promise. Don't make it.
3. **The demo is real.** If the outreach says "we built a demo of an AI receptionist for you," it exists and uses their real hours/services. AI voice demos must not impersonate the owner or staff.
4. **Disclose AI.** Voice agents and SMS identify as an automated assistant for [Business]. Check current law on AI disclosure where the business operates.
5. **Compliance before launch.** Recording consent, TCPA/consent for texts, A2P 10DLC registration, DNC. These change; always label as "check current law" and recommend the client confirm with counsel. See `references/compliance-risk.md`.

## Outreach rules (same as Vanguard)

DNC-check every number, call 8am–9pm their local time, text only after a clear verbal yes, cold email with real sender, postal address and opt-out, stop all touches on any reply or opt-out, log in the CRM the same day.

## How to work with the user

- Ask which business/niche and which offer before writing anything.
- For a discovery call, give the script and an empty calculator. Fill it only with numbers the user says the prospect gave.
- For pricing, ask for the agency's rates. Example prices in references are labelled examples; don't present them as market data.
- For delivery, produce a build spec, not a promise of how long it takes, unless the user gives their delivery timelines.

## Quality checklist

- [ ] One primary offer, tied to a pain the owner said out loud
- [ ] Every ROI input came from the prospect (or is labelled as an assumption they agreed)
- [ ] Results shown as a range with conservative case first
- [ ] Price uses the agency's rates; examples labelled
- [ ] AI disclosure, consent and SMS registration flagged in the proposal
- [ ] Handoff spec lists integrations, logins needed and escalation path to a human
