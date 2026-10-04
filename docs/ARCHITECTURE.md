# Architecture

```
Request -> Step 0 Discovery gate -> design-brief.md (CONFIRMED, frozen)
              |                          |
      (interview with user)              v
                                 Phase 1 Direction   (anthropic-frontend-design)
                                 Phase 2 System      (Pro Max engine -> MASTER.md)
                                 Phase 3 Build       (shadcn/ui + Magic UI)
                                 Phase 4 Review      (Impeccable detect / critique / polish)
```

## Principles
1. One owner per phase, so sources never compete.
2. Precedence: user brief > persisted project files (MASTER.md, PRODUCT.md, DESIGN.md) > direction > engine data.
3. One design system and one component base (shadcn/ui) per project.
4. The stricter accessibility rule always wins.
5. The brief is frozen after confirmation; later changes are scoped edits.

## Layout
| Path | Purpose |
|---|---|
| `SKILL.md` | Router, conflict rules, workflow |
| `agents/mh-web-designer.md` | Autonomous builder agent |
| `references/discovery.md` | Discovery interview and brief template |
| `references/impeccable/` | Playbooks, helper agents, launcher (`scripts/`) |
| `references/shadcn/`, `references/magic-ui/` | Component skills |
| `engine/` | Pro Max search scripts and CSV data; `FALLBACK-no-python.md` |
| `licenses/`, `NOTICE.md` | Third-party licenses and attribution |

## Why the agent needs a brief
Sub-agents cannot ask the user questions. Discovery therefore runs in the main conversation; the agent builds only from a confirmed brief and stops with `NEEDS_DISCOVERY` otherwise.
