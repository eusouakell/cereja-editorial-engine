from pathlib import Path
import json,hashlib,shutil
p=Path(__file__).resolve().parent
url='https://www.instagram.com/p/DePRsywlchM/'
master=p/'agent-runtime-identity-variant-2-final.png'
assert hashlib.sha256(master.read_bytes()).hexdigest()==json.loads((p/'variant-2-final-verification.json').read_text(encoding='utf-8'))['sha256']
proof=p/'publication-evidence';proof.mkdir(exist_ok=True)
base=Path('C:/Users/Kell/Documents/Codex/2026-09-30/github-plugin-github-openai-curated-remote')
for name in ['instagram-agent-runtime-shared.png','instagram-agent-runtime-published.png']:
 shutil.copy2(base/name,proof/name)
record=json.loads((p/'decision-record.json').read_text(encoding='utf-8'))
record['state']='observing'
record['decision']['publication_status']='published; observing; edits require new Kell gate'
record['decision']['publication']={'permalink':url,'account':'cerejaflamejante','published_at_utc':'2026-10-08T15:39:47.000Z','published_at_local':'2026-10-08T12:39:47-03:00','timezone':'America/Sao_Paulo','time_source':'Instagram rendered time element datetime','share_clicked_at_utc':'2026-10-08T15:39:38.936Z','authorization':'Kell explicitly replied pode publicar after final preview','native_tags':['itau','googlecloud','googlecloudlatam','santodigital'],'collaboration_invitation':False,'ai_label':True,'crop':'4:5','grid_preview':'not available before publishing in native web creation flow','caption':'approved caption verbatim; Markdown bold syntax rendered as plain text; no wording changes','alt':'approved alt entered and observed on published profile tile','post_publish_edits':False}
record['observed_outcome']='Instagram confirmed Seu post foi compartilhado.; permalink opened and caption, four native tags and AI label verified. Published 2026-10-08 at 12:39:47 America/Sao_Paulo. Audience performance not yet measured.'
record['learn_back']=[x for x in record['learn_back'] if not x.startswith('Pending final publish-package') and not x.startswith('Publish-package verification completed;')]
record['learn_back'].append('Human-in-the-loop final send completed: Kell explicitly authorized only after preview. Global and LATAM Google Cloud tags both selected by Kell. No post-publication creative/content edits.')
record['evidence'] += [url,'growth/cycles/agent-runtime-identity-production/publication-evidence/instagram-agent-runtime-shared.png','growth/cycles/agent-runtime-identity-production/publication-evidence/instagram-agent-runtime-published.png']
(p/'decision-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
package=(p/'publish-package.md').read_text(encoding='utf-8')
package=package.replace('Publication: **not published / not scheduled**. Final Kell publish gate required.',f'Publication: **PUBLISHED** — [Instagram post]({url}). 2026-10-08, **12:39:47 BRT**. Kell explicitly authorized the final send. State: **observing**. No edits without a new gate.')
package=package.replace('Final master frozen for review; Kell publish authorization remains pending.','Final master frozen; published after Kell authorization.')
package+='\n## Publication execution record\n\nNative Instagram confirmed sharing. Four photo tags verified on the published post: `@itau`, `@googlecloud`, `@googlecloudlatam` (both Google accounts explicitly authorized by Kell), `@santodigital`. Itaú and global Google Cloud showed verification badges; SantoDigital profile identified its Google Cloud partner role and event context. Caption and alt preserved; AI label enabled; no collaborator invited. The native web flow did not offer a separate pre-publication grid preview. Checklist above is the preparation record; publication evidence and current state are recorded here and in Decision Record. Supporting Story was not created or published by this task.\n'
package=package.replace('Nothing is published by this execution.','Final send authorized by Kell and completed; no edits without new gate.')
(p/'publish-package.md').write_text(package,encoding='utf-8')
readme=(p/'README.md').read_text(encoding='utf-8')
readme=f'# Published cycle status\n\nState: **observing**. [Instagram post]({url}) published 2026-10-08 at **12:39:47 BRT**, after Kell explicitly replied “pode publicar”. Caption, asset and alt remain unchanged. Four native tags and AI label verified; no collab. Any subsequent caption/asset edit requires a new Kell gate.\n\nThe execution/preflight notes below are historical. Current publication evidence is in `publication-evidence/` and `decision-record.json`.\n\n'+readme
(p/'README.md').write_text(readme,encoding='utf-8')
print('Recorded published permalink/time; decision state observing; master hash unchanged')
