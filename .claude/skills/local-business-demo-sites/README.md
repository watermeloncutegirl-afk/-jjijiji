# local-business-demo-sites

A Claude Code skill for building honest, clearly labelled demo websites for local
businesses that have no proper website, then publishing each one to its own
Netlify URL.

- `SKILL.md` is the skill itself (frontmatter plus the full workflow). This is the
  file Claude loads.
- `templates/` holds the shared files every demo needs (`_headers`, `robots.txt`)
  plus a worked example: `example-penryn-mot.html` and `example-research.md`.
- `reference/PROMPT.md` is the standing brief to paste at the start of a session,
  with the credit line, working folder and hosting details to fill in.
- `reference/SKILLS-USED.md` lists the companion skills and tools the workflow
  leans on.

## Installing

Copy the skill folder (not this repo path) into a skills directory Claude reads:

```bash
cp -r .claude/skills/local-business-demo-sites ~/.claude/skills/
```

Kept in `.claude/skills/` in this repository it also loads automatically for any
Claude Code session working in this checkout, including cloud sessions, which
otherwise start with an empty `~/.claude/skills`.

## What the workflow needs at runtime

The research and deploy steps reach outside the sandbox, so a session needs:

1. A browser Claude can drive and that is signed in where needed: the in-app
   browser in the Claude desktop app, or Claude in Chrome. Google Maps reviews,
   owner photos, Facebook and Instagram are all rendered client side, so a plain
   HTTP fetch will not do.
2. Netlify CLI with a logged-in account, for one site per business.
3. Python with Pillow for resizing and rotating the downloaded photos, and a
   local HTTP server plus a preview browser for the 375px and desktop checks.

A cloud session with no linked browser can still write, verify and commit a demo
from research that has already been gathered, but it cannot do step 1 itself.
