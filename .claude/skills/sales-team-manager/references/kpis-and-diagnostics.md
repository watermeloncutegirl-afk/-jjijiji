# KPIs and diagnostics

## The KPI tree

```
Cash collected
└── Closes × average cash per close
    └── Qualified shows × close rate
        └── Booked demos × show rate × qualification rate
            └── Conversations × booking rate
                └── Connects (owner reached) × conversation rate
                    └── Dials × connect rate
```

Plus two speed and quality measures:
- **Speed-to-lead** (for inbound or callback requests): time from lead/request to first call. Faster is almost always better; measure it in minutes.
- **Callback discipline:** % of promised callbacks made at the exact time promised.

## Definitions (write them down so everyone counts the same way)

| Metric | Definition |
|---|---|
| Dials | Outbound calls placed |
| Connects | A human answered (front desk counts) |
| Owner conversations | Spoke with the decision-maker for 30+ seconds |
| Booked | Demo on the closer's calendar with confirmed time + link sent |
| Show | Decision-maker attended |
| Qualified show | Show that meets the agreed qualification rules |
| Close | Signed + first payment received |
| Cash collected | Money received in the period |

## Setting targets: use your own data

Don't adopt "industry benchmarks" as truth. Gong-type stats are mostly B2B and vary wildly by niche, list quality and time of day.

1. Track 2 weeks of honest data per rep.
2. Use the **team median** as the baseline and the **top rep** as the stretch.
3. Set targets per rep stage (ramping vs. certified).
4. Revisit monthly.

[EXAMPLE] daily targets for a certified setter (calibrate before using): 80–120 dials, 15–25 owner conversations, 2–4 booked. These are placeholders only.

## Diagnostic decision tree

Always find the **first** broken step in the funnel and fix it before anything downstream.

**Low dials**
- Check: time on phone vs. scheduled block, list ready before the block, dialer setup.
- Causes: call reluctance, admin creep, bad list prep.
- Actions: pre-built lists the day before, power hours, manager on the floor first 30 min.

**Low connect rate**
- Check: time of day vs. niche timing rules (salons 2–4pm Tue–Thu, trades early/lunch/after 5, restaurants 2–4pm), number reputation (spam-flagged caller ID), list quality.
- Actions: move blocks to the niche windows, rotate/register numbers, clean lists.

**Connects but few owner conversations (stuck at the front desk)**
- Check tape: is name + company in the first sentence? Does the rep sound like they belong (slow, statements down)? Do they get the gatekeeper's name and a callback time?
- Drill: the `vanguard-gatekeeper` smokescreen rapid-fire.

**Owner conversations but few bookings**
- Check tape: opener length (under 10 s?), honest permission opener vs. "how's your day?", is the demo hook clear ("we already built it"), two-option booking ask, does the rep stop talking after asking?
- Also check price handling: dodging twice loses calls; quoting off-policy numbers creates bad bookings.
- Drill: `vanguard-cold-call-opener`, `vanguard-price-question`.

**Bookings but low show rate**
- Check: was the link sent during the call and confirmed ("did that come through?")? Was the up-front contract set? Reminder sequence in GHL (confirmation right away, reminder the day before, reminder ~1 hour before)? Time from booking to demo (shorter is usually better)?
- Actions: same-day/next-day demo slots, a confirmation call or text (text only with consent), setter personally confirms.

**Shows but low qualification**
- Check: are setters asking 2–3 fit questions (owner? taking new customers? ~$2,000 in range?) Is setter comp paying per booking instead of per qualified show?
- Actions: tighten the qualification definition, fix comp, tape-review unqualified shows with the setter.

**Qualified shows but low close rate**
- Check the closer's tape against CLOSER: did they clarify and label, or jump into the demo? Did they sell the outcome before the features? Which buying condition (works / trust / money) keeps failing?
- If one closer is fine and another isn't → closer skill. If all closers drop at once → offer, demo quality, price or lead quality changed.

**Closes but low cash collected**
- Check: payment taken on the call vs. "I'll send an invoice", failed payments, refund rate.
- Actions: take the first payment during R (Reinforce), tighten invoicing, review what's promised in the close.

**Good numbers, bad outcomes (refunds, complaints, angry reviews)**
- Check tape for overpromising, invented urgency, off-policy discounts. Treat as a serious performance issue even if the rep is a top seller.

## Team problem or rep problem?

| Pattern | Likely cause |
|---|---|
| Everyone dropped the same week | List, offer, number reputation, season, process change |
| One rep far below the rest on one step | That rep's skill at that step → targeted drill |
| One rep low on activity, fine on conversion | Will/effort or schedule problem → 1:1 |
| One rep high on bookings, low on shows/qualified | Booking junk to hit numbers → check comp and tape |

## DIAGNOSE output template

```
Funnel (period: __)            Team      Rep A     Rep B
Dials
Connect rate
Owner conv. rate
Booking rate (per owner conv.)
Show rate
Qualified rate
Close rate
Cash collected

Bottleneck: <first broken step>
Evidence to pull: <which 3 calls, which report>
Actions (owner, by when):
1.
2.
3.
Re-measure: <metric, date>
```
