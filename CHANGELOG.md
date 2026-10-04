# Changelog

All notable changes to this project. Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [SemVer](https://semver.org/).

## [1.0.0] - 2026-10-04
### Added
- Unified router `SKILL.md` with four phases and eight ordered conflict rules.
- Full discovery interview (`references/discovery.md`, 25 questions in 6 batches) that produces a frozen `design-brief.md`.
- `mh-web-designer` autonomous agent that refuses to start without a confirmed brief.
- Bundled UI UX Pro Max engine and data, Anthropic `frontend-design`, Impeccable (references, helper agents, launcher), shadcn/ui and Magic UI skills.
- No-Python fallback (`engine/FALLBACK-no-python.md`).
- Installers, CI (engine tests, data validation, link check), docs, licenses and NOTICE.

### Fixed (compared with the first import)
- Paths with spaces, CRLF line endings in scripts, upstream-only tests removed, broken internal links, invalid search-domain names, shadcn context line made conditional, Impeccable template placeholders resolved.
- A confirmed brief now satisfies Impeccable's `init` and interview directives.

### Verified
- 137 engine tests pass; shadcn and Magic UI install plus build verified; discovery-to-agent flow exercised end to end with a simulated brief.
