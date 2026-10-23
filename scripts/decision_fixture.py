#!/usr/bin/env python3
"""Offline development double for decision orchestration, never inference.
Fixture outputs are predefined test data. No network/provider/backend dependency.
"""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--fixture',required=True);p.add_argument('action',choices=['submit','status']);a=p.parse_args()
 f=Path(a.fixture);s=json.loads(f.read_text())
 if not s.get('synthetic_decision_fixture'):raise ValueError('Unmarked fixture')
 if a.action=='status':
  s['status_checks']=s.get('status_checks',0)+1
  result={'request_id':s['request_id'],'status':s['request_status'],'results':s.get('results',[]),'synthetic':True}
 else:
  s['submissions']=s.get('submissions',0)+1
  result={'request_id':s['request_id'],'status':s.get('submit_status','completed'),'synthetic':True}
  if result['status']=='completed':result['results']=s.get('results',[])
 f.write_text(json.dumps(s,indent=2));print(json.dumps(result))
if __name__=='__main__':main()
