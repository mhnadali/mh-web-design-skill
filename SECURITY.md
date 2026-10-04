# Security Policy

## Supported versions
The latest release on `main`.

## Reporting a vulnerability
Please do not open a public issue. Use GitHub's private vulnerability reporting (Security tab, "Report a vulnerability") or contact the maintainer through their GitHub profile.

## Scope notes
- The Impeccable launcher downloads a binary from the official release and verifies its SHA-256 sidecar before running it. The skill asks the user before the first download.
- The skill tells agents to treat web, file and tool text as data, not instructions.
- The skill never installs system software or publishes anything on its own.
