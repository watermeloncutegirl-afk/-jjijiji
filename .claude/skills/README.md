# Vanguard Sales Skills

Claude Code skills for training setters and running a setter→closer sales team. They are built from the Vanguard Studios setter training (modules 01–03 plus the fundamentals), the Hormozi sales material, and the research in [`SALES_SKILLS_RESEARCH.md`](../../SALES_SKILLS_RESEARCH.md).

The skills load automatically when you use Claude Code in this repo. To use them everywhere, copy them into your user skills folder:

```bash
cp -r .claude/skills/* ~/.claude/skills/
```

## Skills

| Skill | For | Modes | Try saying |
|---|---|---|---|
| [`vanguard-gatekeeper`](vanguard-gatekeeper/SKILL.md) | Module 01: getting past the front desk | Prep · Roleplay · Review | "Role-play a suspicious spouse at a roofing company" |
| [`vanguard-cold-call-opener`](vanguard-cold-call-opener/SKILL.md) | Module 02: the first 30 seconds, rapport and booking | Prep · Roleplay · Review | "Write my opener for Tasha's Salon in Austin" |
| [`vanguard-price-question`](vanguard-price-question/SKILL.md) | Module 03: "What does it cost?" | Prep · Roleplay · Review | "Run the two-ask price drill" |
| [`vanguard-setter-coach`](vanguard-setter-coach/SKILL.md) | Ground rules, drills, full-call role-play, the 100-point scorecard, 14-day onboarding | Drill · Roleplay · Review · Onboard | "Review my call" / "Train a new setter" |
| [`sales-team-manager`](sales-team-manager/SKILL.md) | Hormozi-style management of setters and closers: hiring, comp, KPIs, CLOSER, call review | Advise · Build · Diagnose · Run session | "My show rate is 45%, what's broken?" |
| [`hormozi-offer-builder`](hormozi-offer-builder/SKILL.md) | $100M Offers for agency services: value equation, Grand Slam Offer, guarantees | Build · Audit · Objection-proof | "Audit our web design offer" |
| [`web-design-agency-sales`](web-design-agency-sales/SKILL.md) | The demo-first pipeline: lead list → audit → demo brief → outreach → demo call → proposal → kick-off | Pipeline templates | "Build a lead list for barbers in Tampa" |
| [`ai-automation-agency-sales`](ai-automation-agency-sales/SKILL.md) | Selling AI automations to local businesses: offer menu, ROI discovery, pricing, n8n and voice handoff | Pipeline templates | "Run an ROI discovery for a towing company" |

## Rules every skill enforces

- **Honesty:** say the setter's name and Vanguard in the first sentence. Never fake callbacks, referrals, familiarity or urgency, and never pretend to be Google. If you ask a skill for a deceptive tactic, it refuses and gives you the honest version.
- **Approved numbers only:** a typical build is around $2,000, one-time; a bigger build is around $2,600; the optional care plan is about $200/mo, cancel anytime; the demo is free; the site goes live 14 days after the kick-off call. Prices, discounts and terms are [Closer]'s call.
- **Compliance:** only call numbers that have been checked against the do-not-call list, and only from 8am to 9pm their time. Text only after a clear verbal yes. If someone says "Don't call me", add them to the do-not-call list the same day. Log every call in GHL the same day.
- **No invented statistics:** example figures are labelled as examples, and secondary-source claims are flagged.

## Built by us, not from the training

Some content was designed for these skills and isn't in the training doc: the scoring rubrics and their point weights, the "25 words or fewer" stand-in for "under 10 seconds", the Day 10 certification bar (80 or more on every call, with no hard fails), the role-play personas, and the example comp plans. Adjust them to match how you actually run the team.
