# How to use the Vanguard sales skills

There are 8 skills in `.claude/skills/`. Each one is a folder with a `SKILL.md` and supporting files. Claude loads a skill automatically when what you ask matches it. You don't need a special command; just ask naturally.

## 1. Download

You can download them in either of these ways:
- **GitHub:** open the repo, switch to the branch `claude/busy-fermi-cmvj2e`, then click **Code → Download ZIP**.
- **Command line:**
  ```bash
  git clone -b claude/busy-fermi-cmvj2e https://github.com/watermeloncutegirl-afk/-jjijiji.git
  ```

## 2. Install

### Claude.ai (web, desktop or mobile app)
1. Make each skill its own zip, with the folder at the top level (for example `vanguard-gatekeeper.zip` containing `vanguard-gatekeeper/SKILL.md`). The per-skill zips are already built this way.
2. Go to **Settings → Capabilities** (called **Customize** in some versions) **→ Skills**. Turn on code execution if Claude asks you to.
3. Click **Upload skill** and upload each zip. Upload all 8, because they refer to each other.

### Claude Code (terminal)
To use the skills in every project:
```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/* ~/.claude/skills/
```
Inside this repo, they already work with nothing to install. Run `/skills` (or ask "what skills do you have?") to check they loaded.

### Sharing with your team
Send setters the zips, or put the folders in your team's shared repo under `.claude/skills/`.

## 3. Which skill to use when

| You want to… | Say something like | Skill that loads |
|---|---|---|
| Prep a call for a specific business | "Prep my call for Mike's Roofing in Dallas. 4.6 stars, no website." | `vanguard-cold-call-opener` |
| Practise the front desk | "Role-play a busy salon receptionist, level 2." | `vanguard-gatekeeper` |
| Practise the price question | "Run the two-ask price drill." | `vanguard-price-question` |
| Do daily drills | "Run my setter drills for today." / "Rapid-fire smokescreens." | `vanguard-setter-coach` |
| Practise a full call from start to finish | "Full cold-call role-play, towing company, difficulty 4." | `vanguard-setter-coach` |
| Get a call scored | Paste the transcript or notes, then say "Review my call." | `vanguard-setter-coach`, or the module skill that fits |
| Onboard a new setter | "Start the 14-day onboarding for a new setter named Sam." | `vanguard-setter-coach` |
| Manage the team | "Build a commission plan for 3 setters and 1 closer." / "Here are this week's numbers, what's broken?" | `sales-team-manager` |
| Coach your closer | "Run a CLOSER role-play where the owner says 'I need to ask my wife.'" | `sales-team-manager` |
| Improve your offer | "Audit our web design offer with the value equation." | `hormozi-offer-builder` |
| Find leads | "Build a lead list plan for barbers in Tampa." / "Audit this prospect: [Google listing]" | `web-design-agency-sales` |
| Write follow-ups or proposals | "Write the follow-up email sequence." / "Write a proposal for Tasha's Salon." | `web-design-agency-sales` |
| Sell AI automations | "Run an ROI discovery call for an HVAC company." / "Price a missed-call text-back offer." | `ai-automation-agency-sales` |

## 4. Suggested daily routine for setters (30 minutes)
1. **5 minutes:** "Opener drill." Record yourself saying it 10 times; Claude checks the length and wording.
2. **10 minutes:** "Rapid-fire smokescreens." Claude reads the 10 in random order; you answer each one, starting with the ledge.
3. **5 minutes:** "Two-ask price drill."
4. **10 minutes:** one full-call role-play in today's niche.
5. **After your shift:** paste one booked call, one hang-up and one "send me info" call, and say "Review these calls."

## 5. Customising
The scoring point weights, the 25-word opener limit, the Day 10 certification bar and the example comp plans were designed for these skills, not taken from the training. To change any of them, edit the relevant `references/*.md` file. If prices change, update every skill. Find every mention with:
```bash
grep -rn "two thousand\|twenty-six hundred\|two hundred a month" .claude/skills
```
