# M.H. Web Design Skill

[![CI](https://github.com/mhnadali/mh-web-design-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/mhnadali/mh-web-design-skill/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-skill%20%2B%20agent-orange)
![License](https://img.shields.io/badge/license-MIT%20%2B%20Apache--2.0%20components-green)

**One Claude Code skill and one autonomous agent for professional UI/UX and web design**: websites, landing pages, SaaS products, dashboards, apps and design systems.

It combines five best-in-class open-source projects behind a single router with explicit conflict rules, and adds a full **discovery interview** so the design is right the first time and is never rebuilt from scratch.

## Why

| Problem | How this skill handles it |
|---|---|
| AI designs look generic | Direction rules from Anthropic `frontend-design` plus Impeccable's anti-pattern detector |
| Redesigns burn time and tokens | A 25-question discovery produces a **frozen, confirmed `design-brief.md`** before any design work |
| Several design skills fight each other | One owner per phase, eight ordered conflict rules, one design system, one component base |
| Output isn't buildable | Builds with shadcn/ui and Magic UI, checked with `npm run build` |
| No quality gate | Impeccable `detect` plus critique/audit/polish, an accessibility floor and a bounded visual check |

## What's inside

| Phase | Owner | Location |
|---|---|---|
| 0. Discovery | This repo | [`references/discovery.md`](references/discovery.md) |
| 1. Direction | Anthropic `frontend-design` | [`references/anthropic-frontend-design.md`](references/anthropic-frontend-design.md) |
| 2. Design system | UI UX Pro Max engine (192 industry rules, 192 palettes, 74 font pairings, 22 stacks) | [`engine/`](engine/) |
| 3. Build | shadcn/ui and Magic UI | [`references/shadcn/`](references/shadcn/), [`references/magic-ui/`](references/magic-ui/) |
| 4. Review | Impeccable (about 40 playbooks, mechanical anti-pattern detector) | [`references/impeccable/`](references/impeccable/) |
| Autonomous builder | `mh-web-designer` agent | [`agents/mh-web-designer.md`](agents/mh-web-designer.md) |

The router and conflict rules live in [`SKILL.md`](SKILL.md). See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Install

Requirements: [Claude Code](https://claude.com/claude-code); Python 3 (standard library only; optional, there is a no-Python fallback); Node 18+ for building UIs.

**Windows (PowerShell)**
```powershell
git clone https://github.com/mhnadali/mh-web-design-skill "$HOME\.claude\skills\mh-web-design-skill"
New-Item -ItemType Directory -Force "$HOME\.claude\agents" | Out-Null
Copy-Item "$HOME\.claude\skills\mh-web-design-skill\agents\mh-web-designer.md" "$HOME\.claude\agents\" -Force
```

**macOS / Linux**
```bash
git clone https://github.com/mhnadali/mh-web-design-skill ~/.claude/skills/mh-web-design-skill
mkdir -p ~/.claude/agents && cp ~/.claude/skills/mh-web-design-skill/agents/mh-web-designer.md ~/.claude/agents/
```

Or run the bundled [`install.ps1`](install.ps1) / [`install.sh`](install.sh) from a clone. Then **start a new Claude Code session**, because skills load at session start.

## Use

1. **Hands-on (skill):** type `/mh-web-design-skill` and describe what you want, for example *"design a fintech analytics dashboard"*. Claude runs the discovery interview (brand kit, audience, goals, style references, content, stack), writes `design-brief.md`, shows a direction summary, and builds after you confirm.
2. **Hands-off (agent):** once the brief is confirmed, ask for the `mh-web-designer` agent to build it. It refuses to start without a confirmed brief, because sub-agents cannot ask questions.
3. **Later changes** are scoped edits (`polish`, `colorize`, `typeset`, `layout`, `bolder`, `quieter`, `distill`, `audit`, `critique`) on named targets, never a redesign, unless you reopen the brief.

### Engine examples
```bash
python engine/scripts/search.py "fintech analytics dashboard" --design-system --persist -p "Ledger" --output-dir . --density 9
python engine/scripts/search.py "revenue trend" --domain chart
python engine/scripts/search.py "dashboard table" --stack shadcn
python engine/scripts/validate_data.py
```

## Notes and first-run behavior
- **Impeccable engine:** on first use its launcher downloads a SHA-256-verified binary from the official [pbakaus/impeccable](https://github.com/pbakaus/impeccable) release into `~/.impeccable`. The skill asks before the first download; without it, reviews fall back to the written playbooks.
- **shadcn and Magic UI** are installed per project through `npx shadcn@latest` (network needed).
- **Quote your paths:** the skill's commands quote paths because home folders may contain spaces.

## Verified
The Pro Max engine tests (137) and data validation pass. shadcn `init`/`add`, Magic UI components and a production build were verified in a scratch project. The discovery-to-agent flow was exercised end to end with a simulated brief (see the [CHANGELOG](CHANGELOG.md)). CI re-runs the engine tests, data validation and a link check on every push.

## Credits and licenses
This project bundles unmodified or lightly adapted content from these projects, each under its own license (copies in [`licenses/`](licenses/), details in [`NOTICE.md`](NOTICE.md)):

| Project | License |
|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT |
| [anthropics/skills](https://github.com/anthropics/skills) (`frontend-design`) | Apache-2.0 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | MIT |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | MIT |

The original work in this repo (router, discovery interview, conflict rules, agent, installers, docs) is released under the [MIT License](LICENSE). Bundled third-party content keeps its own license.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Release history is in [CHANGELOG.md](CHANGELOG.md).
