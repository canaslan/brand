# Can Aslan — Brand

Public documents and resources for my design principles and visual identity.

This repository includes my design principles, color system, and typography tokens. Further brand and identity documentation will be added as it is ready.

## Start here

- [Design principles](principles.md): beliefs that guide my work.
- [Visual identity](identity/README.md): visual direction and identity resources.
- [Color](identity/color/README.md): palette, semantic tokens, import guidance, and validation.
- [Typography](identity/typography/README.md): typefaces, shared tokens, and units.

## Repository structure

```mermaid
flowchart LR
    n0["brand/"]
    n0 --> n1["#46;#103;#105;#116;#104;#117;#98;"]
    n1 --> n2["#119;#111;#114;#107;#102;#108;#111;#119;#115;"]
    n2 --> n3["#114;#101;#112;#111;#45;#100;#105;#97;#103;#114;#97;#109;#46;#121;#109;#108;"]
    n0 --> n4["#46;#103;#105;#116;#105;#103;#110;#111;#114;#101;"]
    n0 --> n5["#76;#73;#67;#69;#78;#83;#69;"]
    n0 --> n6["#82;#69;#65;#68;#77;#69;#46;#109;#100;"]
    n0 --> n7["#105;#100;#101;#110;#116;#105;#116;#121;"]
    n7 --> n8["#82;#69;#65;#68;#77;#69;#46;#109;#100;"]
    n7 --> n9["#99;#111;#108;#111;#114;"]
    n9 --> n10["#82;#69;#65;#68;#77;#69;#46;#109;#100;"]
    n9 --> n11["#99;#111;#108;#111;#114;#115;#46;#116;#111;#107;#101;#110;#115;#46;#106;#115;#111;#110;"]
    n9 --> n12["#99;#111;#110;#116;#114;#97;#115;#116;#45;#114;#101;#112;#111;#114;#116;#46;#106;#115;#111;#110;"]
    n9 --> n13["#118;#97;#108;#105;#100;#97;#116;#101;#46;#112;#121;"]
    n7 --> n14["#116;#121;#112;#111;#103;#114;#97;#112;#104;#121;"]
    n14 --> n15["#82;#69;#65;#68;#77;#69;#46;#109;#100;"]
    n14 --> n16["#116;#121;#112;#111;#103;#114;#97;#112;#104;#121;#46;#116;#111;#107;#101;#110;#115;#46;#106;#115;#111;#110;"]
    n0 --> n17["#112;#114;#105;#110;#99;#105;#112;#108;#101;#115;#46;#109;#100;"]
    n0 --> n18["#115;#99;#114;#105;#112;#116;#115;"]
    n18 --> n19["#117;#112;#100;#97;#116;#101;#45;#114;#101;#112;#111;#45;#100;#105;#97;#103;#114;#97;#109;#46;#112;#121;"]
```

## Working with this repo

Keep design principles in `principles.md` and visual identity resources in `identity/`. Keep each identity resource's guidance, source files, and supporting tools together, as the color folder does.

Edit color values in `identity/color/colors.tokens.json`, then run this command from the repository root:

```sh
python3 identity/color/validate.py
```

Commit the regenerated contrast report with token changes. Any future CSS or other platform exports should be generated from the token source rather than maintained as separate palettes.

Add logos, imagery, or component documentation when those resources exist. A separate component design system is not part of v1.0. Use lowercase, hyphen-separated filenames and relative Markdown links between documents.

## License

See [LICENSE](LICENSE).
