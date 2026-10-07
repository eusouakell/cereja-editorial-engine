# Web production specs

Status: Cereja house standard.  
Last reviewed: **2026-10-07**.

Web is not a fixed-canvas channel. Production requirements therefore focus on responsive behavior, source assets and share previews rather than one page dimension.

Use Flame for UI/experience rules.

## Social / Open Graph preview

**House standard**
- default preview master: **1200 × 630 px / 1.91:1**
- sRGB
- JPEG or PNG
- keep key text, faces and brand marks away from extreme edges because downstream social platforms may crop differently.

This is an interoperability house standard, not a claim that every destination crops identically.

## Raster images

Preferred delivery:
- AVIF/WebP when browser/support pipeline is controlled;
- JPEG for photography fallback;
- PNG for transparency or graphic assets where lossless rendering matters.

Requirements:
- intrinsic width/height declared;
- responsive source sizes when appropriate;
- no oversized source shipped merely because the master is large;
- alt text for meaningful imagery;
- empty alt only when the image is truly decorative.

## Vector

- SVG preferred for approved vector brand/interface assets when available.
- Canonical Cereja flame/signature assets must not be redrawn or regenerated.
- Do not expose font files or licensed source assets publicly beyond their permitted scope.

## Motion/video

- poster frame required where appropriate;
- captions/transcript when audio carries meaning;
- reduced-motion alternative for motion that affects experience;
- performance budget and lazy loading as applicable.

## Responsive safe area

There is no single pixel safe area.

The implementation must preserve:
- headline/CTA readability at narrow widths;
- focal-point-aware image crop;
- brand-mark legibility;
- no essential meaning at clipped edges;
- reflow/zoom behavior under Flame accessibility requirements.

## Content prerequisites

- approved content hierarchy;
- alt text;
- rights/provenance;
- social preview;
- metadata/title/description;
- current destination/link validation;
- accessibility and performance checks.
