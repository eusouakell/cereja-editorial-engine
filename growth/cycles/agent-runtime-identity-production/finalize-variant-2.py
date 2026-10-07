from pathlib import Path
import sys,json,hashlib,shutil,io
from PIL import Image,ImageCms,ImageDraw

p=Path(__file__).resolve().parent
edited=Path(sys.argv[1])
shutil.copy2(edited,p/'source/variant-2-text-removed-master.png')
profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
im=Image.open(edited).convert('RGB')
if im.size!=(1080,1350):im=im.resize((1080,1350),Image.Resampling.LANCZOS)
final=p/'agent-runtime-identity-variant-2-final.png'
im.save(final,icc_profile=profile)
im.save(p/'agent-runtime-identity-variant-2-final.jpg',quality=95,subsampling=0,icc_profile=profile)
im.resize((390,488),Image.Resampling.LANCZOS).save(p/'variant-2-final-mobile.png',icc_profile=profile)
qa=im.copy();ImageDraw.Draw(qa).rectangle((72,72,1008,1278),outline='#00A6A6',width=2)
qa.save(p/'variant-2-final-safe-area.png',icc_profile=profile)
out=Image.open(final)
assert out.size==(1080,1350) and out.mode=='RGB'
assert 'sRGB' in ImageCms.getProfileName(ImageCms.ImageCmsProfile(io.BytesIO(out.info['icc_profile'])))
(p/'variant-2-final-verification.json').write_text(json.dumps({'dimensions':[1080,1350],'mode':'RGB','color_profile':'sRGB','safe_area_px':72,'sha256':hashlib.sha256(final.read_bytes()).hexdigest(),'critical_content_safe_area':'visual inspection required','publication':'not published / not scheduled'},indent=2),encoding='utf-8')
record=json.loads((p/'decision-record.json').read_text(encoding='utf-8'))
record['decision']['creative_review']={'verdict':'PASS','selected_variant':'variant 2','recorded_result':'Creative Director: PASS — variant 2','authority':'Creative Director review supplied by Kell; Kell confirmed variant 2 = PNG at commit 564fdc8','required_revision':'Remove only identidade · autoridade · estado · observabilidade; no replacement or recomposition','master_ref':'growth/cycles/agent-runtime-identity-production/agent-runtime-identity-variant-2-final.png'}
record['decision']['publication_status']='not published / not scheduled; pending Kell publish gate'
record['evidence'] += ['growth/cycles/agent-runtime-identity-production/publish-package.md','growth/cycles/agent-runtime-identity-production/agent-runtime-identity-variant-2-final.png','growth/cycles/agent-runtime-identity-production/variant-2-final-verification.json']
record['observed_outcome']='Creative Director: PASS — variant 2. Kell selected the variant and requested removal of the supporting block only. Final publish gate remains pending; no audience outcome measured.'
record['learn_back']=[x for x in record['learn_back'] if x!='Pending independent Creative Director review.']
record['learn_back'].insert(0,'Creative review accepted the selected direction; remove redundant supporting copy without opening another route.')
(p/'decision-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
package=(p/'publish-package.md').read_text(encoding='utf-8').replace('Pending exact identification of the selected variant 2 and removal of the supporting text block. Do not publish the previous export by mistake.','Master: `agent-runtime-identity-variant-2-final.png`. Creative Director: **PASS — variant 2**. Kell confirmed the selected base is the PNG at commit `564fdc8`; only the supporting block was removed. Earlier exports are historical, not publication masters.\n\nExport: 1080×1350, RGB with embedded sRGB; 72 px critical-content inset. See `variant-2-final-verification.json` and annotated safe-area image.').replace('Alt must be confirmed against the selected final variant before publication.','Alt matches the final composition after removal of the supporting block. Recheck when entering it in-app.')
(p/'publish-package.md').write_text(package,encoding='utf-8')
print('Final export and decision/package updated')
