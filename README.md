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
    root["brand/"]
    root --> readme["README.md"]
    root --> principles["principles.md"]
    root --> identity["identity/"]
    root --> license["LICENSE"]
    root --> ignore[".gitignore"]

    identity --> identity_readme["README.md"]
    identity --> color["color/"]
    identity --> typography["typography/"]

    color --> color_readme["README.md"]
    color --> color_tokens["colors.tokens.json"]
    color --> validator["validate.py"]
    color --> report["contrast-report.json"]

    typography --> typography_readme["README.md"]
    typography --> typography_tokens["typography.tokens.json"]
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
