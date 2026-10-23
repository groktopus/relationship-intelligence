#!/usr/bin/env python3
"""Offline structural validation; never a semantic-quality or harness claim."""
import hashlib,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
errors=[];checks=[]
def check(ok,message):
    checks.append({'check':message,'passed':bool(ok)})
    if not ok:errors.append(message)
s=(root/'SKILL.md').read_text();parts=s.split('---',2)
check(len(parts)==3,'YAML frontmatter delimiters')
front=parts[1] if len(parts)==3 else ''
check(bool(re.search(r'^name: relationship-intelligence$',front,re.M)),'canonical name matches directory')
check(root.name=='relationship-intelligence','canonical directory name')
check('description:' in front and 'license: Apache-2.0' in front,'description and license declared')
check(len(s.splitlines())<500,'core below500 lines')
check(len(s.split())<1500,'concise core word boundary')
for n in ['README.md','LICENSE','CONTRIBUTING.md','AGENTS.md','SECURITY.md','docs/traceability.md','docs/release-evidence.md','evals/evals.json','evals/trigger-cases.json']:
    check((root/n).is_file(),'required artifact '+n)
check('Apache License' in (root/'LICENSE').read_text() and 'Version 2.0, January 2004' in (root/'LICENSE').read_text(),'Apache 2.0 license text')
for p in root.rglob('*.md'):
    if '.git' in p.parts:continue
    text=p.read_text()
    if p.parent.name=='references':check(len(text)<=60000,'reference size '+str(p.relative_to(root)))
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if target.startswith(('http:','https:','mailto:','#')):continue
        target=target.split('#')[0]
        if target:check((p.parent/target).exists(),'relative link '+str(p.relative_to(root))+' -> '+target)
    check(not re.search(r'/(?:Users|home)/[^/\s]+/',text) and not re.search(r'(?i)bearer\s+[A-Za-z0-9_-]{20,}',text),'no private artifacts '+str(p.relative_to(root)))
e=json.loads((root/'evals/evals.json').read_text())['evals']
check([x['id'] for x in e]==list(range(1,23)),'finite release suite22 unique ordered cases')
for x in e:check(all(k in x for k in ['prompt','expected_output','assertions','host_setup','capabilities','permissions']),'case fields '+str(x['id']))
methods='\n'.join(p.read_text() for p in (root/'references').glob('*.md'))
ids=re.findall(r'^## MC-(\d+):',methods,re.M)
check(sorted(ids)==[f'{i:02}' for i in range(1,12)],'eleven unique method contracts')
tr=json.loads((root/'evals/trigger-cases.json').read_text())
# Preserve schema flexibility; triggers are separately human/harness evaluated.
check(bool(tr),'trigger suite present')
files=sorted(p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts)
h=hashlib.sha256()
for p in files:h.update(str(p.relative_to(root)).encode()+b'\0'+p.read_bytes()+b'\0')
print(json.dumps({'kind':'structural_only','content_sha256':h.hexdigest(),'checks':len(checks),'failed':errors},indent=2))
sys.exit(bool(errors))
