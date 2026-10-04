#!/bin/sh
# Installs the skill and agent into ~/.claude (run from the repo root).
set -eu
SRC=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DEST="$HOME/.claude/skills/mh-web-design-skill"
mkdir -p "$HOME/.claude/skills" "$HOME/.claude/agents"
if [ "$SRC" != "$DEST" ]; then
  rm -rf "$DEST"
  mkdir -p "$DEST"
  (cd "$SRC" && tar --exclude=.git -cf - .) | (cd "$DEST" && tar -xf -)
fi
cp "$DEST/agents/mh-web-designer.md" "$HOME/.claude/agents/"
echo "Installed to $DEST. Start a new Claude Code session, then use /mh-web-design-skill"
