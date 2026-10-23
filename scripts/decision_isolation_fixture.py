#!/usr/bin/env python3
"""Development-only typed-request/failure fixture, not model inference.
Accepts exact synthetic request data; records per-handler inputs and validations.
No network or production adapter. Results are deterministic fixture responses.
"""
import argparse,copy,hashlib,json,math
from pathlib import Path

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()

def valid_answer(contract,answer,span_ids):
    if answer.get('type')!=contract['type']:raise ValueError('type mismatch')
    t=contract['type']
    if t=='choice':
        if answer.get('choice') not in contract['criteria']:raise ValueError('choice outside contract')
    else:
        field='score' if t=='score' else 'noul';v=answer.get(field)
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):raise ValueError('nonfinite/nonnumeric result')
        upper=len(contract['criteria'])-1 if t=='score' else 1
        if not 0<=v<=upper:raise ValueError('result outside anchors')
    if not set(answer.get('span_ids',[]))<=span_ids:raise ValueError('unknown grounding span')

def fixture_handler(handler_input, fault=None):
    """Actual isolated callable: no access to the caller's answers mapping.
    Literal checks are fixture mechanics, not model inference.
    """
    packet=handler_input['evidence_packet'];contract=handler_input['contract']
    spans={s['span_id']:s['text'] for s in packet['response_spans']}
    if packet['source_id']!='R1' or packet['question_id']!='Q1' or packet['context']!='release Z only':raise ValueError('wrong fixture evidence')
    if fault=='noul_exception':raise TimeoutError('injected single-handler timeout')
    t=contract['type']
    if t in ('choice','score'):
        if spans.get('S1')!='A written comparison first' or spans.get('S2')!='then let us discuss it':raise ValueError('fixture evidence mismatch')
        if t=='choice':return {'type':'choice','choice':'mixed','span_ids':['S1','S2']}
        return {'type':'score','score':'not an ordinal' if fault=='invalid_score' else 2,'span_ids':['S1','S2']}
    if t=='noul':
        if spans.get('S3')!='approval from security before choosing':raise ValueError('fixture prerequisite mismatch')
        return {'type':'noul','noul':1.0,'span_ids':['S3']}
    raise ValueError('unsupported fixture contract')

def execute(request,mode):
    if request.get('fixture')!='case15-local-v1':raise ValueError('unmarked synthetic request')
    packet=request['evidence_packet'];questions=request['questions']
    if set(questions)!={'preparation_mode','ordering','security_prerequisite'}:raise ValueError('unexpected case15 contracts')
    if {v['type'] for v in questions.values()}!={'choice','score','noul'}:raise ValueError('mixed types missing')
    if not all(q.get('version') and q.get('instructions') for q in questions.values()):raise ValueError('unversioned/undefined contract')
    if not isinstance(questions['preparation_mode'].get('criteria'),dict) or not isinstance(questions['ordering'].get('criteria'),list):raise ValueError('malformed criteria')
    if 'answers' in packet or 'results' in packet:raise ValueError('sibling results embedded in evidence')
    original=fingerprint(packet);span_ids={s['span_id'] for s in packet['response_spans']};answers={};trace=[]
    for name,contract in questions.items():
        # Each handler input is newly copied from original evidence and its own
        # contract. The accumulated answers object is never an input.
        handler_input={'evidence_packet':copy.deepcopy(packet),'contract':copy.deepcopy(contract)}
        trace.append({'question_id':name,'input':copy.deepcopy(handler_input),'input_sha256':fingerprint(handler_input)})
        try:
            fault=mode if (mode=='invalid_score' and name=='ordering') or (mode=='noul_exception' and name=='security_prerequisite') else None
            answer=fixture_handler(handler_input, fault)
            valid_answer(contract,answer,span_ids)
            answers[name]={'status':'valid','answer':answer,'contract_version':contract['version']}
        except (ValueError,TimeoutError) as exc:
            answers[name]={'status':'unknown','answer':None,'error_type':type(exc).__name__,'error':str(exc),'contract_version':contract['version']}
    assert fingerprint(packet)==original
    unresolved=[k for k,v in answers.items() if v['status']!='valid']
    return {'synthetic':True,'inference':False,'mode':mode,'request_sha256':fingerprint(request),'evidence_sha256':original,'handler_inputs':trace,'answers':answers,'dependent_stage':{'status':'deferred' if unresolved else 'ready_for_main_agent','unresolved_prerequisites':unresolved,'constructed_candidates':None}}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--request',required=True);p.add_argument('--mode',choices=['normal','invalid_score','noul_exception'],required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=execute(json.loads(Path(a.request).read_text()),a.mode);Path(a.output).write_text(json.dumps(result,indent=2));print(json.dumps({'mode':a.mode,'statuses':{k:v['status'] for k,v in result['answers'].items()},'dependent_stage':result['dependent_stage']['status'],'synthetic':True,'inference':False}))
if __name__=='__main__':main()
