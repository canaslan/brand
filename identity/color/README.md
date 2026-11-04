# Can Aslan color tokens

Corrected color system exported from the supplied Figma variable snapshot on 2026-10-11. The Figma file was not changed. This package contains colors only.

## Import into Penpot

1. Open a test file in Penpot, then the **Tokens** panel.
2. Choose **Tools → Import** and select `colors.tokens.json`.
3. Select **Color mode → Light** or **Dark**. Base must remain enabled; enable only one semantic theme at a time.
4. Bind semantic tokens to your layers and components.

Import can replace the existing token setup, so export existing tokens first if using an established file. The bundle follows Penpot's documented `$type`, `$value`, `$description`, `$themes`, and `$metadata` format with hex sRGB values. It has been validated locally; a live Penpot import has not been performed. It is a Penpot-compatible interchange bundle, not a claim of strict conformance to the latest standalone DTCG color-object schema.

Reference: https://penpot.app/blog/a-practical-guide-to-the-design-tokens-json-format/

## Files and source of truth

- `colors.tokens.json`: edit this file as the canonical source. 43 shared primitives and 51 semantic tokens defined in each theme (94 distinct token names, 145 definitions).
- `validate.py`: dependency-free Python validator for aliases, theme parity, and declared contrast pairs.
- `contrast-report.json`: generated contrast results. Regenerate after changing colors.

The original export notes describe four `status/<name>` foreground tokens becoming `color.status.<name>.default` so the same group can contain text, icon, border, and background tokens without mixing a token and a group. Primitive names gain the `color.` prefix, as do semantic names. Figma scopes and code-syntax metadata are not portable Penpot token fields and are not copied. The original `figma-name-map.json` was not supplied with this repository, so coverage of all 57 original Figma names cannot currently be verified.

## Applied fixes

- Light tertiary text: grey/600; dark tertiary remains grey/400.
- Light accent/default link text: orange/800; hovered links: orange/900.
- Dark default links: orange/500 for more contrast margin; hovered links: orange/400.
- Visited links: purple/700 in light, purple/300 in dark.
- New `color.border.control`: grey/500 in light, grey/400 in dark; intended for boundaries on default and subtle surfaces. Decorative borders retain their original values.
- New button foregrounds: grey/900 for default/hovered; grey/50 for pressed orange/700.
- Four statuses now have separate text, icon, border, background, and compatibility foreground roles. New primitive shades provide theme-specific readable status colors.
- Original orange, grey, and status primitives are preserved. Duplicate primitive modes are represented once in Base.

## Required component bindings

Importing JSON does not migrate or rebind existing Figma or Penpot components. Apply `color.button.foreground.default` to both button labels and icons in default/hovered states, and `color.button.foreground.pressed` in pressed states. Existing `text.on-accent` stays dark and must not be used on orange/700. Use `border.control` where a visible boundary identifies a control, and status role tokens for their documented purposes.

Readable foregrounds are validated on `surface.default` and `surface.subtle`, not every possible background. The darker/lighter hovered and pressed surface tokens need context-specific foreground choices. Focus colors are checked against page surfaces; a focus indicator next to an orange control still needs a contrasting offset or two-color treatment. Disabled text and decorative borders are not required to pass these tests. Opacity, image/gradient backgrounds, blending, text sizing, interaction behavior, and non-color status cues must be checked in the final UI.

## Validate locally or in CI

```sh
python3 identity/color/validate.py
```

Run this command from the repository root. The validator compares unrounded ratios against 4.5:1 for normal text and 3:1 for relevant icons/borders. It regenerates the report beside the tokens and exits nonzero on failure. Guidance: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html and https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

## Repository maintenance

This package lives under `identity/color/` in the [brand repository](../../README.md). Keep its guidance, canonical tokens, validator, and generated report together. Generated CSS can be added later; derive it from the JSON instead of maintaining a second palette manually. See the repository's existing [MIT license](../../LICENSE).
