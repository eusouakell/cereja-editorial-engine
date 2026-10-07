# Substack / newsletter production specs

Status: operational.  
Last reviewed: **2026-10-07**.

Official Substack sources reviewed:
- optimal image dimensions: https://support.substack.com/hc/en-us/articles/4408381685268-What-are-the-optimal-image-dimensions-for-my-Substack-publication
- image/media support: https://support.substack.com/hc/en-us/articles/360037832971-How-do-I-embed-media-in-my-post-e-g-images-video-GIFs
- email header/footer banners: https://support.substack.com/hc/en-us/articles/360056142311-How-do-I-edit-email-headers-and-footers-on-Substack
- video embeds: https://support.substack.com/hc/en-us/articles/15659757294228-How-do-I-embed-a-video-in-a-Substack-post
- file attachments: https://support.substack.com/hc/en-us/articles/4408381643156-How-can-I-attach-a-file-to-my-Substack-post
- Notes media: https://support.substack.com/hc/en-us/articles/14743550626580-Can-I-add-images-GIFs-or-video-to-a-Substack-note

## Publication identity

**Official verified**
- publication logo: at least **256 × 256 px**, transparent background recommended
- email banner: **1100 × 220 px** recommended, transparent background; may be taller
- welcome-page cover: at least **600 × 600 px**
- current profile header: at least **1344 × 256 px**, minimum 3:2 source aspect noted by Substack profile-theme documentation
- wordmark: at least **1344 × 256 px** in current theme guidance

Flame optical-brand rules still apply. Do not force the complete Cereja signature into a surface where it becomes unreadable.

## Post / social preview image

Substack's current official help article contains an internal inconsistency: it recommends **at least 1200 × 630 px** while also stating **14:10** for preview images. Those are not the same ratio.

**Cereja operational decision**
- use **1200 × 630 px** as the current social-preview production default because it is the explicit pixel recommendation;
- mark the crop as **verify_in_app** before publish;
- keep title/face/key object away from extreme edges;
- use Substack's center/smart-cropping controls when needed.

Do not silently convert the conflicting 14:10 statement into a new ratio rule.

## Inline / full-width images

**Official verified**
- supported image uploads include: **AVIF, GIF, JPG/JPEG, PNG, WEBP**
- Substack states that full-width images taller than **1:1** may be automatically cropped to **1:1**

**Cereja house standard**
- photo-dominant: JPEG/WebP as appropriate
- graphic/type-heavy: PNG
- keep a high-resolution source master outside Substack
- verify email and app rendering with a test send

## Email banner

**Official verified**
- **1100 × 220 px PNG** is explicitly recommended by current Substack email header/footer guidance.

## Video in article

**Official verified**
- accepted types include 3GP, AAC, AVI, FLV, MP4, MOV and MPEG-2
- Substack recommends a maximum upload size of **20 GB**

**Cereja house standard**
- MP4 delivery preferred
- captions/transcript retained whenever speech carries meaning
- check email fallback/thumbnail behavior before send

## File embeds

**Official verified**
- Substack accepts file attachments including PDF, EPUB, XLSX, CBR/CBZ and other listed formats
- file thumbnail images are cropped to **3:2**

## Notes

**Official verified**
- up to **6 images/GIFs** in a Note
- GIF availability can differ by client
- one video per Note
- current video upload limit for Notes: **5 minutes**

## Content prerequisites

Before publication:
- approved newsletter/post copy;
- current facts rechecked;
- rights/provenance;
- accessible image descriptions;
- test email;
- link check;
- preview/crop inspection;
- brand-mark legibility;
- source URLs retained in the production record even when public credit is shorter.
