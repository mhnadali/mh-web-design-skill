# M.H. Web Design Skill

A single Claude skill for UI/UX and design across websites, SaaS, apps and dashboards.

Pipeline: **Direction** (Anthropic frontend-design) → **System** (UI UX Pro Max engine) → **Build** (shadcn/ui + Magic UI) → **Review** (Impeccable).

## Install
Copy this folder to `~/.claude/skills/mh-web-design-skill` (global) or `<project>/.claude/skills/mh-web-design-skill`. Requires Python 3 for the design-system engine.

## Try it
> Design a SaaS analytics dashboard for a fintech startup.

See `SKILL.md` for the conflict rules, and `NOTICE.md` for licenses.

## Bundled and tested
- UI UX Pro Max engine (`engine/`): 164 upstream tests pass, data validates; no-Python fallback in `engine/FALLBACK-no-python.md`.
- Impeccable engine launcher (`references/impeccable/scripts/`): downloads a SHA-256-verified binary from the official release on first use; `context` and `detect` verified.
- shadcn/ui and Magic UI: `init`, `info`, `docs`, `add card sidebar chart table @magicui/marquee @magicui/blur-fade` and a production build verified in a scratch Vite project.
