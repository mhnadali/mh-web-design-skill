# Contributing

Thanks for helping. Keep changes small and focused.

## Ground rules
- `SKILL.md` is the router: keep it short, ordered and unambiguous. Detail belongs in `references/`.
- Do not edit bundled third-party content (`engine/data`, `references/impeccable`, `references/shadcn`, `references/magic-ui`, `references/anthropic-frontend-design.md`) except for path or placeholder fixes. Prefer upstreaming changes.
- Any new bundled content must be MIT or Apache-2.0 (or compatible), with its license in `licenses/` and an entry in `NOTICE.md`.
- Quote paths in every command (they may contain spaces). Use LF line endings.

## Before opening a PR
```bash
python engine/scripts/validate_data.py
cd engine/scripts/tests && python -m unittest discover -s .
python .github/scripts/check_links.py
```
Update `CHANGELOG.md` and, for user-visible changes, bump `VERSION`.

## Reporting issues
Use the issue templates. Include your OS, Claude Code version, and the exact command or prompt.
