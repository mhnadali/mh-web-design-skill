# Fallback when Python 3 is not available

The engine is only a search layer over plain CSV files in `engine/data/`. Without Python, query them directly with the Grep and Read tools (never install Python yourself).

## Manual design-system recipe
1. `products.csv`: Grep the product type (e.g. "SaaS", "fintech", "healthcare") → note `Primary Style Recommendation`, `Landing Page Pattern`, `Dashboard Style`, `Color Palette Focus`.
2. `ui-reasoning.csv`: Grep the same `UI_Category` → `Recommended_Pattern`, `Style_Priority`, `Color_Mood`, `Typography_Mood`, `Decision_Rules`, `Anti_Patterns`.
3. `styles.csv`: Grep the recommended style name → effects, best-for, do-not-use-for, light/dark support.
4. `colors.csv`: Grep the product type → complete token set (Primary, Secondary, Accent, Background, Foreground, Card, Muted, Border, Destructive, Ring and their On-* pairs).
5. `typography.csv`: Grep mood keywords → heading/body fonts, Google Fonts URL, CSS import, Tailwind config. `google-fonts.csv` has 1,934 families for custom picks.
6. `landing.csv` (section order, CTA placement), `charts.csv` (chart type per data type, accessibility fallback), `motion.csv`, `icons.csv` as needed.
7. `ux-guidelines.csv`, `app-interface.csv`, `react-performance.csv`: Grep by `Category`/`Issue`/`Keywords`; apply `Do` and avoid `Don't`.
8. `stacks/<stack>.csv` (shadcn, react, nextjs, vue, svelte, html-tailwind, flutter, swiftui and more): Grep `Category`/`Guideline`.

Use `Grep -i "<term>"` with `output_mode: content` on one CSV at a time; each row is one record, the first line is the header. Persist the result by hand in `design-system/<project>/MASTER.md`.

## Columns
- products: Product Type, Keywords, Primary Style Recommendation, Secondary Styles, Landing Page Pattern, Dashboard Style, Color Palette Focus, Key Considerations
- styles: Style Category, Type, Keywords, Primary/Secondary Colors, Effects & Animation, Best For, Do Not Use For, Light/Dark Mode, Performance, Accessibility
- colors: Product Type + 17 token columns
- typography: Font Pairing Name, Heading Font, Body Font, Mood/Style Keywords, Google Fonts URL, CSS Import, Tailwind Config
- ux-guidelines / app-interface: Category, Issue, Platform, Description, Do, Don't, Severity
- charts: Data Type, Best Chart Type, When to Use, Accessibility Grade, A11y Fallback, Library Recommendation
