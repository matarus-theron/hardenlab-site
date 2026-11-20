# HardenLab website

Bilingual Hugo/Hextra website for **HardenLab Local Pack**, at `https://www.hardenlab.ch/`.

## Develop and build

Use Hugo Extended **0.156.0** and Go **1.26** (matching the Pages workflow).

```sh
hugo server --disableFastRender
hugo --gc --minify
python3 scripts/check_site.py public
```

The **Check website** workflow runs the build and internal link checks on pull requests targeting `main`. It checks that the German and English homepages render and reports missing pages and anchors. It can also be run manually from the Actions tab.

German is the default language at `/`; English lives at `/en/`. Content uses Hugo's filename suffix model (`buy.md`, `buy.en.md`). The theme is pinned in `go.mod`.

- `data/marketing.json`: German and English landing page and pricing labels.
- `data/plans.yaml`: shared planned CHF prices and device counts.
- `layouts/_shortcodes/`: landing and pricing components.
- `layouts/home.html`, `layouts/single.html`, `layouts/marketing.html`: page structure; each page has one H1 supplied by its layout or landing component.
- `assets/css/custom.css`: responsive brand styling, including light/dark and keyboard focus states.
- Search is disabled through Hextra’s supported configuration. With only a hidden mobile search input, Hextra 0.12.1 throws on desktop keyboard events; the compact site uses navigation and footer links instead.

## Current status and release checklist

The site is a **pre-launch product preview**. There are no checkout links or pre-orders. Do not imply that the product can already be purchased. Pricing is non-binding; support and update commitments remain open.

Before sales start:

1. Confirm the actual released installer, supported Windows versions, known limitations and recovery instructions against product documentation. Current documentation targets 26H2 and 25H2; the site does not claim fresh Windows validation.
2. Confirm final prices, tax treatment, delivery, license scope and any included support/update period.
3. Have provider identification, privacy disclosures, the German license and its English translation, and terms reviewed. Provider details are currently limited to the brand, locality and contact email at the owner's request. The absence of sales does not establish that those details satisfy applicable information duties. Supply the required operator identity/address before relying on these pages as final legal notices; do not invent a legal entity or personal details.
4. Specify actual hosting, email, checkout and license-processing providers and processes in the privacy policy.
5. Update availability messages in both languages, connect and verify the real purchase/delivery flow, and only then enable sales.
6. Verify German and English navigation, footer links, metadata, mobile layout, keyboard focus and theme switching. Check that the owner's personal name has not been reintroduced unintentionally.

A push to `main` triggers the existing GitHub Pages deployment. Build locally for review; publishing requires a separate instruction.
