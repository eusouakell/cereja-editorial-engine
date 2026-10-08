from pathlib import Path
from PIL import Image,ImageCms
import json,io,hashlib
p=Path(__file__).resolve().parent
master=p/'agent-runtime-identity-variant-2-final.png'
original=master.read_bytes()
im=Image.open(master)
assert im.size==(1080,1350) and im.mode=='RGB'
assert 'sRGB' in ImageCms.getProfileName(ImageCms.ImageCmsProfile(io.BytesIO(im.info['icc_profile'])))
verification=json.loads((p/'variant-2-final-verification.json').read_text(encoding='utf-8'))
assert hashlib.sha256(original).hexdigest()==verification['sha256']
verification['reconfirmed_at']='2026-10-08 America/Sao_Paulo'
verification['master_unchanged']=True
verification['creative_review']='Creative Director: PASS FINAL — variant 2'
(p/'variant-2-final-verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record=json.loads((p/'decision-record.json').read_text(encoding='utf-8'))
record['decision']['creative_review']['final_verdict']='PASS FINAL'
record['decision']['creative_review']['final_review_date']='2026-10-08'
record['decision']['creative_review']['recorded_result']='Creative Director: PASS FINAL — variant 2'
record['decision']['creative_review']['freeze']='No further creative changes; current PNG is final master.'
record['observed_outcome']='Creative Director: PASS FINAL — variant 2 after removal of the supporting block. Master frozen; publication remains pending. No audience outcome measured.'
(p/'decision-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
package=(p/'publish-package.md').read_text(encoding='utf-8').replace('Creative Director: **PASS — variant 2**.','Creative Director: **PASS FINAL — variant 2**, confirmed by Kell on 2026-10-08. Master frozen; no further creative changes.')
package=package.replace('- [ ] Confirm selected final PNG, 1080×1350, embedded sRGB, 72 px critical-content inset.','- [x] Final PNG reconfirmed on 2026-10-08: 1080×1350, embedded sRGB, 72 px critical-content inset; SHA-256 unchanged.')
package=package.replace('## Mentions — verify in-app before publishing','## Credits / provenance\n\nFinal artwork: synthetic editorial illustration edited with built-in image generation from the visual proof supplied and approved by Kell. The portrait and system fields are conceptual; they are not a real participant or runtime verification record. No third-party logo added. For the documentary Story, record photographer/source and applicable permission before use; do not infer the photographer from the filename.\n\n## Mentions — verify in-app before publishing')
(p/'publish-package.md').write_text(package,encoding='utf-8')
readme=(p/'README.md').read_text(encoding='utf-8').replace('Status: **Creative Director: PASS — variant 2**.','Status: **Creative Director: PASS FINAL — variant 2**, confirmed 2026-10-08. Master frozen; no further creative changes.')
(p/'README.md').write_text(readme,encoding='utf-8')
caption=(p/'caption-approved.md').read_text(encoding='utf-8').split('## Final caption\n\n')[1].split('\n## Publication notes')[0].strip()
assert caption==package.split('## Approved caption\n\n')[1].split('\n## Alt text')[0].strip()
assert master.read_bytes()==original
print('PASS: master unchanged; 1080x1350 sRGB; caption unchanged; final creative review recorded')
