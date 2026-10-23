#!/usr/bin/env python3
"""Development-only synthetic host. Never a runtime memory backend.
Reads/writes only an explicitly initialized .synthetic-host fixture directory.
No network, credentials, connector, or source-import behavior.
"""
import argparse, copy, hashlib, json, os, sys
from pathlib import Path

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',required=True)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('capabilities')
    r=sub.add_parser('read');r.add_argument('--view',default='canonical')
    a=sub.add_parser('apply');a.add_argument('--change-file',required=True)
    args=ap.parse_args();root=Path(args.root).resolve()
    if not (root/'.synthetic-host').is_file():
        raise ValueError('Not an initialized synthetic fixture; no operation performed')
    p=root/'state.json';state=json.loads(p.read_text())
    if args.command=='capabilities':
        print(json.dumps({'mode':state['mode'],'views':list(state['views']), 'faults':state.get('faults',{}),'permissions':state['permissions']}));return
    if args.command=='read':
        if state['mode'] in ('none','write-only') and args.view!='audit':
            print(json.dumps({'status':'unavailable','reason':'no read capability'}));return
        if args.view=='audit':
            if state['mode']=='write-only':
                print(json.dumps({'status':'unavailable','reason':'no verification capability'}));return
            print(json.dumps({'status':'ok','audit':state['audit']}));return
        if args.view in state.get('faults',{}).get('unavailable_views',[]) or args.view in state.get('faults',{}).get('read_blocked_views',[]):
            print(json.dumps({'status':'unavailable','reason':'synthetic view unavailable'}));return
        print(json.dumps({'status':'ok','view':args.view,'records':state['views'].get(args.view,{}),'revision':state['revision']}));return
    if state['mode'] not in ('read-write','write-only'):
        print(json.dumps({'status':'denied','reason':'fixture has no write permission'}));sys.exit(2)
    change_path=Path(args.change_file).resolve()
    if not change_path.is_relative_to(root):
        raise ValueError('Change file must be inside this synthetic fixture')
    change=json.loads(change_path.read_text())
    ident=change['operation_id'];ops=change['operations']
    if any(e['operation_id']==ident for e in state['audit']):
        print(json.dumps({'status':'already_applied','operation_id':ident}));return
    before=digest(state['views']);residual=[]
    for op in ops:
        view=op['view'];key=op['key']
        if state.get('allowed_keys') and key not in state['allowed_keys']:
            raise ValueError('Key outside fixture-authorized scope')
        if view in state.get('faults',{}).get('unavailable_views',[]) or view in state.get('faults',{}).get('write_blocked_views',[]):
            residual.append({'view':view,'key':key});continue
        target=state['views'].setdefault(view,{})
        if op['action']=='set':target[key]=copy.deepcopy(op['value'])
        elif op['action']=='remove':target.pop(key,None)
        else:raise ValueError('Unsupported synthetic action')
    state['revision']+=1
    state['audit'].append({'operation_id':ident,'before_hash':before,'after_hash':digest(state['views']),'residual':residual})
    uncertain=state.get('faults',{}).get('uncertain_once',False)
    if uncertain:state['faults']['uncertain_once']=False
    tmp=root/'state.tmp';tmp.write_text(json.dumps(state,indent=2));os.replace(tmp,p)
    print(json.dumps({'status':'uncertain' if uncertain else ('partial' if residual else 'confirmed'),'operation_id':ident,'residual':residual,'revision':state['revision']}))
    if uncertain:sys.exit(2)

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError,json.JSONDecodeError) as e:
        print(json.dumps({'status':'error','reason':str(e)}));sys.exit(2)
