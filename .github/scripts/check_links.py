"""Fail if a relative markdown link points to a missing file."""
import os
import re
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
bad = 0
for dp, dn, fs in os.walk(root):
    dn[:] = [d for d in dn if d not in (".git", "node_modules")]
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        text = open(p, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", text):
            link = m.group(1)
            if re.match(r"(https?:|mailto:)", link):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(dp, link))):
                bad += 1
                print(f"BROKEN {os.path.relpath(p, root)} -> {link}")
print("broken links:", bad)
sys.exit(1 if bad else 0)
