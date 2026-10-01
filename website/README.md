# Cereja Flamejante — website

Static public entry point for the newsletter and context projects. Substack remains the publishing and subscription service.

## Files and preview

`index.html`, `style.css` and `assets/` are the deployable files. Run `python -m http.server 8765 --directory website` from the repository root and open http://localhost:8765.

Brand images were supplied by Kell from the Cereja brand assets. No third-party font files are bundled. Do not republish these assets as an independent brand kit.

## Deployment

Hosting: existing HostGator account, domain https://cerejaflamejante.com.br/. Upload only the deployable files to this domain's confirmed document root. Do not upload README, private files, credentials or this repository as a whole. Review changes and keep a rollback copy before replacing production files. Domain-specific redirect configuration is managed separately in cPanel.

The first site version was published previously. This PR versions its source and proposes a small contrast correction; merging does not deploy it automatically.

## Validation and limits

Static checks passed: Portuguese page language, one h1, unique IDs, valid internal fragment links, existing image sources and alt attributes, stylesheet presence, keyboard focus styling and reduced-motion CSS. Two responsive breakpoints are present; that alone does not certify mobile usability.

Palette calculation found white on original pink (#EA1945) at 4.45:1, below 4.5:1 for normal text. Button and subscription backgrounds are changed to #BE1035; the original pink remains an accent. Ink on lime is 8.08:1 and ink on white 11.37:1.

Screen-reader testing, browser viewport/zoom checks, live external-link checks and measured performance remain pending. Do not describe this as a full accessibility audit or claim a Lighthouse score.

No analytics, tracking, JavaScript, API integration or embedded forms. No TreeID or client content.
