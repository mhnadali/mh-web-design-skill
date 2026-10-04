# Discovery: get the full brief before any design work

Goal: know exactly what the user wants BEFORE building, so the design is never redone. Discovery is thorough on purpose; a few minutes of questions saves hours of rework and tokens.

**Rules**
- Run this in the MAIN conversation, with the user. A subagent cannot ask questions, so it must never do discovery; it builds only from a confirmed brief.
- Skip a question only if the user's request, the repo (PRODUCT.md, DESIGN.md, design-system/, existing code, brand files) or an earlier answer already settles it. Say what you inferred.
- Ask in batches. Choice questions go through the structured question tool (AskUserQuestion, at most 4 per call, 2-4 options each, put your recommendation first). Open questions (names, hex codes, links, copy) go in chat as a short numbered list.
- Every question accepts "you decide". Record each such answer as an ASSUMPTION in the brief; never silently invent a preference.
- When the user supplies a URL, screenshot, Figma, logo or brand file, inspect it (browser tool, Read for images) and extract colors, fonts, spacing, tone. Quote findings back for confirmation.
- Do not start the build until the user confirms the finished brief.

## Batch 1: Product and purpose (chat or structured)
1. Product/company name and one-line description. What exactly is this design (landing page, marketing site, web app, SaaS dashboard, admin, mobile app, component, design system, redesign of existing)?
2. The primary job of the surface: what must the visitor or user be able to do? What is the single most important action (sign up, buy, book, monitor, create)?
3. Success metric: what makes this design a win (conversion, task speed, trust, retention)?
4. Scope: which pages/screens/states are needed now (list them), and what is explicitly out of scope? New build or redesign of an existing product (get the URL/repo)?

## Batch 2: Audience
5. Who is it for (role, age range, expertise, industry, region)? Who is it explicitly NOT for?
6. Context of use: desktop at work, phone on the move, shared screen, long sessions, high stakes (money, health)? Devices and browsers that matter.
7. Language(s), and any RTL (Persian, Arabic, Hebrew) or multi-language needs. Currency/date/number formats.
8. Accessibility target (WCAG AA default, AAA, specific needs).

## Batch 3: Brand kit (the most important batch)
9. Does a brand kit exist? Ask for: logo files, brand colors (hex), fonts, tone of voice, brand guidelines, Figma/URL, existing marketing, imagery style. If none: "create one for me" or "partial".
10. Brand personality: pick up to 3-4 words (e.g. trustworthy, playful, premium, calm, bold, technical, warm, minimal). And 2-3 words it must NOT feel like.
11. Color: fixed brand colors, preferred hues, colors to avoid, light mode, dark mode, or both (default mode?). Contrast with competitors desired or avoided?
12. Typography: fixed fonts, or preference (serif, sans, geometric, humanist, mono accents, display personality)? Licensing limits? Non-Latin script needs?
13. Imagery and iconography: photography, illustration, 3D, abstract, data-visual, none. Icon library preference (lucide, phosphor, custom). Logo usage rules.
14. Voice and copy: do real copy and data exist, or should placeholders be written? Formal, friendly, concise, playful? Any claims, legal text or compliance wording that must appear or be avoided.

## Batch 4: Visual style and references
15. Style direction (choose from the Pro Max styles, show 3-4 relevant options with one-line descriptions): e.g. minimal/editorial, glassmorphism, bento grid, brutalism, neumorphism, dark OLED, data-dense, soft/rounded, retro, luxury. Density: spacious, balanced, dense. Corner radius: sharp, soft, pill. Motion: none, subtle, expressive.
16. References: 2-5 sites/apps/dribbble/screens they love and what exactly they like about each (color, layout, typography, motion, feel). 1-3 they dislike and why. Direct competitors to resemble or differ from.
17. Hard dos and don'ts (e.g. "no gradients", "no stock photos", "no purple", "must feel like Stripe-level polish").
18. Level of ambition: safe and conventional, polished but distinctive, or bold and unusual.

## Batch 5: Content, features and structure
19. Information architecture: navigation items, sections per page, key components (hero, pricing, tables, charts, forms, onboarding, empty/error states, settings, auth).
20. For dashboards/apps: the top 3-5 metrics or tasks, data types, chart types, table needs, filters, roles/permissions, real-time or static data, sample data or API shape.
21. For marketing: offer, proof (logos, testimonials, numbers), CTAs, pricing model, FAQ, legal pages, SEO needs.
22. Interactions and states: loading, empty, error, success, offline, long text, many rows; keyboard and shortcut needs.

## Batch 6: Technical constraints
23. Stack: framework (Next.js, Vite+React, Vue, Svelte, Astro, plain HTML, Flutter, SwiftUI...), CSS approach (Tailwind, CSS modules), component library (shadcn/ui default), TypeScript, package manager, existing repo and conventions, hosting, backend/API/auth in play.
24. Performance and compliance limits (page weight, Core Web Vitals, GDPR/PCI/HIPAA, browser support), analytics or third-party scripts allowed or banned.
25. Deliverable: working code in the repo, a prototype only, a design system/tokens file, Figma-ready specs, or all. Where to put it. Timeline and anything already decided that must not change.

## Finish: lock the brief
1. Write `design-brief.md` in the project root (template below), plus `PRODUCT.md` if the project has none.
2. Run the Pro Max design-system command with the brief's keywords, dials (`--variance`, `--motion`, `--density` mapped from the answers) and persist it, then show the user a compact **direction summary**: palette (hex), fonts, style, layout pattern, motion level, 3 anti-patterns being avoided, and a one-line description of the hero/first screen.
3. Ask the user to confirm or adjust THIS summary (one round). Apply adjustments to the brief and system.
4. Mark the brief `Status: CONFIRMED`. From then on the brief is frozen: later changes are scoped edits (polish, colorize, typeset, layout, bolder, quieter, distill) on named targets, never a redesign, unless the user explicitly reopens the brief.

## design-brief.md template

```markdown
# Design Brief: <Product>
Status: DRAFT | CONFIRMED (<date>)

## Product and purpose
What it is / primary job / key action / success metric / scope / out of scope

## Audience and context
Who / not for / devices / languages (RTL?) / accessibility target

## Brand kit
Logo / colors (hex, roles) / fonts / personality words / must-not-feel / imagery / icons / voice

## Visual direction
Style / density / radius / motion / light-dark / references (like + why) / dislikes / dos and don'ts / ambition

## Structure and content
Pages and screens / navigation / components / states / metrics / sample data

## Technical
Stack / libraries / repo / constraints / deliverable / location

## Assumptions (user said "you decide")
- ...

## Locked design system
Path to design-system/<slug>/MASTER.md and the direction summary as confirmed
```
