# Typography

Use Inter for headings and body text. Use JetBrains Mono for code, captions, metadata, and technical labels.

[Typography tokens](typography.tokens.json) contains the shared type values.

- `font-family` and `font-weight` use typeface and weight names.
- `size` defines named sizes in pixels. `text-size` defines the 1.2 scale in rem.
- `line-height` uses numbers for percentages (100 means 100%). Strings without a unit, such as `"1.6"`, are unitless multipliers.
- `letter-spacing` uses pixels for numbers. Strings include their unit.
- `type-space` defines spacing before headings and between paragraphs in rem.

Page-specific display sizes and responsive rules live in the website project.
