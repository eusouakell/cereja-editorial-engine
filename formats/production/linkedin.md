# LinkedIn production specs

Status: operational.  
Last reviewed: **2026-10-07**.

Official LinkedIn sources reviewed:
- photo posts: https://www.linkedin.com/help/linkedin/answer/a527229/share-photos-or-videos
- media file types: https://www.linkedin.com/help/linkedin/answer/a564109
- document posts: https://www.linkedin.com/help/linkedin/answer/a518909/upload-and-share-documents-on-linkedin
- video sharing: https://www.linkedin.com/help/linkedin/answer/a7174587
- publishing-platform images: https://www.linkedin.com/help/linkedin/answer/a520746/
- Page image specs: https://www.linkedin.com/help/linkedin/answer/a563309/

## Single image post

**Official verified**
- upload limit: **5 MB**
- minimum: **552 × 276 px**
- LinkedIn recommends **1080 px width**
- supported aspect-ratio range: **3:1 through 4:5**
- outside the supported range, the image may be centered/cropped
- alt text can be added in the composer

**Cereja house standard**
- default editorial/social image: **1080 × 1350 px / 4:5**
- sRGB
- PNG for graphic/type-heavy work
- high-quality JPEG for photo-dominant work
- critical-content inset: **72 px**

The 4:5 house standard uses the tallest officially supported photo-post ratio and is intended for strong mobile feed presence.

## Multi-photo post

**Official verified**
- up to **20 images**
- render container max ratio: **4:5**
- layout depends on the first image's orientation
- later images can be cropped depending on the multi-photo layout

For designed sequences, prefer a LinkedIn **document post** rather than depending on multi-photo auto-layout when page-by-page reading order matters.

## Document / swipeable publication

**Official verified**
- accepted: PDF, PPT, PPTX, DOC, DOCX (LinkedIn's broader supported-media docs may list additional formats by surface)
- max file size: **100 MB**
- max pages: **300**

**Cereja house standard**
- preferred delivery for a designed swipeable document: **PDF**
- page canvas: **1080 × 1350 px / 4:5** unless the content requires another deliberate ratio
- critical-content inset: **72 px**
- embed fonts / preserve vector text where possible
- verify PDF page order and accessibility before upload

### Content prerequisites

- document title;
- approved copy;
- readable first page/cover;
- alt/accessibility plan;
- rights/provenance;
- final PDF visual inspection;
- no post-publication dependency on editing the uploaded document, because LinkedIn does not allow replacing/editing it in place.

## Native video

**Official verified**
- max: **5 GB**
- min: **75 KB**
- duration: **3 sec desktop / 2 sec mobile minimum**, up to **15 min**
- resolution: **256 × 144 through 4096 × 2304**
- aspect ratio: **1:2.4 through 2.4:1**
- frame rate: **10–60 fps**
- bitrate: **192 Kbps–30 Mbps**
- LinkedIn explicitly instructs creators to keep top, bottom and side edges clear of key text/logos because UI may overlap them.

**Cereja house master**
- default vertical editorial video: **1080 × 1350 / 4:5** or **1080 × 1920 / 9:16** when full vertical is intentional
- MP4 preferred for operational consistency
- captions required when speech/audio carries meaning

Exact UI safe-zone pixel values are **verify_in_app**; LinkedIn's official guidance is qualitative rather than a single published pixel inset.

## LinkedIn article

**Official verified**
- article image files: JPG, static GIF, PNG
- image max file size: **10 MB**
- ideal cover: **1280 × 720 px**

## URL preview image

**Official verified for Page/custom share previews**
- **1200 × 627 px**
- ratio **1.91:1**
- key content should not depend on extreme edges because crops vary by device/context.

## Page identity surfaces

Current official Page guidance should be rechecked when needed because LinkedIn has changed these dimensions over time.

Do not automatically reuse Cereja social-post art as a Page cover/logo.

## Content prerequisites for any LinkedIn asset

- self-contained post value before outbound link;
- copy provenance preserved;
- rights/provenance complete;
- alt text where supported;
- current preview check;
- brand mark optically legible at final size.
