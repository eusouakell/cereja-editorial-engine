from pathlib import Path
import shutil, json, hashlib
from PIL import Image, ImageCms, ImageDraw

ROOT = Path(__file__).resolve().parent
SRC = Path('C:/Users/Kell/.codex/generated_images/01a0f3af-fc11-72c2-8f3e-6880814dd068/exec-07766e13-40b6-48f6-8d18-beeba439ea08.png')
PROOF = Path('C:/Users/Kell/Downloads/editorial-art-director-approved-proof-v2.png')
(ROOT / 'source').mkdir(exist_ok=True)
shutil.copy2(PROOF, ROOT / 'source/approved-proof-v2.png')
shutil.copy2(SRC, ROOT / 'source/refined-master.png')
profile = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
im = Image.open(SRC).convert('RGB').resize((1080,1350), Image.Resampling.LANCZOS)
im.save(ROOT / 'agent-runtime-identity-1080x1350.png', icc_profile=profile)
im.save(ROOT / 'agent-runtime-identity-1080x1350.jpg', quality=95, subsampling=0, icc_profile=profile)
im.resize((390,488), Image.Resampling.LANCZOS).save(ROOT / 'mobile-preview.png', icc_profile=profile)
qa = im.copy()
ImageDraw.Draw(qa).rectangle((72,72,1008,1278), outline='#00A6A6', width=2)
qa.save(ROOT / 'qa-safe-area.png', icc_profile=profile)
out = Image.open(ROOT / 'agent-runtime-identity-1080x1350.png')
assert out.size == (1080,1350) and out.mode == 'RGB'
assert ImageCms.getProfileName(ImageCms.ImageCmsProfile(__import__('io').BytesIO(out.info['icc_profile']))).strip() == 'sRGB built-in'
(ROOT / 'export-verification.json').write_text(json.dumps({'dimensions':out.size,'mode':out.mode,'icc_profile':'sRGB built-in','safe_area_px':72,'sha256':hashlib.sha256((ROOT / 'agent-runtime-identity-1080x1350.png').read_bytes()).hexdigest()}, indent=2), encoding='utf-8')
print('Export verified: 1080x1350 RGB, embedded sRGB')
