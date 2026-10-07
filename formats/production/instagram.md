# Instagram production specs

Status: operational.  
Last reviewed: **2026-10-07**.

Use with:
- `growth/instagram-strategy-v1.md`;
- `formats/instagram/revista-visual.md`;
- Flame;
- media-rights guard.

## Evidence boundary

Meta's current public documentation is uneven for organic image-post pixel specifications. Therefore:

- feed/static/carousel dimensions below are **Cereja house standards**, not presented as universal Instagram platform law;
- Meta officially supports the 9:16 creative language for Reels and explicitly recommends keeping key messages in a safe zone;
- exact UI chrome and profile-grid crops are treated as **verify_in_app** because they can change.

Official Meta source reviewed:
- Reels: https://www.facebook.com/business/ads/facebook-instagram-reels-ads
- Instagram copyright guidance: https://www.facebook.com/help/354736791367645/
- licensed music / Sound Collection guidance: https://www.facebook.com/help/instagram/402084904469945

## Feed — single static image

**House standard**
- canvas: **1080 × 1350 px**
- aspect ratio: **4:5**
- production color space: **sRGB**
- preferred export:
  - PNG for type/graphic-heavy work;
  - high-quality JPEG for photo-dominant work when file weight materially benefits.
- internal critical-content inset: **72 px from all edges**

The 72 px inset is a Cereja production margin, not an Instagram-published safe-zone number.

### Content prerequisites

Required before publish:
- final approved visual/copy;
- alt text;
- caption;
- rights/provenance status;
- brand-mark decision;
- final mobile-size readability check;
- current in-app feed + profile-grid preview.

### Brand mark

If Cereja Flamejante is already identifiable from account/context and the full signature would be optically small, use the **official isolated flame in negative** when contrast allows.

Do not add the complete signature merely because the piece feels “unbranded”.

## Feed — carousel

**House standard**
- every frame: **1080 × 1350 px / 4:5**
- same canvas for the entire sequence;
- PNG for graphic/type-heavy frames; JPEG allowed for photo-heavy frames;
- internal critical-content inset: **72 px**.

Additional prerequisites:
- approved frame/beat sequence;
- alt text/accessibility plan for the sequence;
- caption/provenance package;
- rights cleared for every frame;
- first and second entry points validated when the format contract requires them;
- no change of story/claim by the renderer.

Current profile-grid and multi-frame preview behavior: **verify_in_app**.

## Stories

**House standard**
- canvas: **1080 × 1920 px**
- aspect ratio: **9:16**
- production color space: sRGB
- static: PNG/JPEG
- motion: MP4 master preferred for delivery

### Conservative Cereja safe area

Because UI chrome varies, keep essential text, logos, faces and tap targets inside:

- left/right: **90 px**
- top: **250 px**
- bottom: **250 px**

These are **house safety margins**, not claimed Meta pixel specifications.

Interactive stickers/links must be positioned after checking the current Instagram composer.

### Content prerequisites

- source/claim traceability;
- rights;
- readable text at phone size;
- link destination tested when used;
- alt/accessibility equivalent where supported;
- no essential meaning hidden under UI chrome.

## Reels / vertical video

Meta explicitly promotes **9:16 vertical video** and keeping key messages in a safe zone for Reels creative.

**House master**
- canvas: **1080 × 1920 px**
- aspect ratio: **9:16**
- preferred delivery: MP4
- captions: required when speech carries meaning
- transcript: retain in production record
- cover/poster: create intentionally; verify current crop in app

### Conservative Cereja safe area

Until exact current organic-Reels chrome is verified in-product:

- left/right: **90 px**
- top: **220 px**
- bottom: **360 px**

Keep headline, face, subtitles and brand mark out of the bottom interaction stack.

These are **house safety margins**, not Meta-published pixel values.

### Content prerequisites

- approved script/story;
- music/audio rights;
- footage rights/provenance;
- subtitle/caption file or burned-in captions as appropriate;
- thumbnail/cover;
- no synthetic footage presented as documentary;
- current in-app preview before publish.

## Deterministic checks we can automate

- expected pixel dimensions;
- aspect ratio;
- allowed export extension;
- presence of required sidecar fields in the production record;
- carousel frame-size consistency.

## Human checks that remain necessary

- optical legibility;
- safe-area survival in current app UI;
- profile-grid crop;
- brand-mark scale;
- art direction;
- rights judgment;
- accessibility equivalence.
