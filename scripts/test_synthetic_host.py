"""Mechanical fixture tests. These do not grade agent behavior."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path
TOOL=Path(__file__).with_name('synthetic_host.py')
class HostTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.r=Path(self.t.name)
        (self.r/'.synthetic-host').write_text('Synthetic test only')
        self.state={'mode':'read-write','permissions':'N1 only','allowed_keys':['N1'],'revision':0,'views':{'canonical':{'N1':'old','N2':'keep'},'search':{'N1':'old'}},'audit':[],'faults':{}}
        self.save()
    def tearDown(self):self.t.cleanup()
    def save(self):(self.r/'state.json').write_text(json.dumps(self.state))
    def call(self,*args):
        r=subprocess.run([sys.executable,str(TOOL),'--root',str(self.r),*args],capture_output=True,text=True)
        return r.returncode,json.loads(r.stdout)
    def change(self,ops):
        p=self.r/'change.json';p.write_text(json.dumps({'operation_id':'same','operations':ops}));return str(p)
    def test_refuses_unmarked_and_outside_change(self):
        (self.r/'.synthetic-host').unlink();code,_=self.call('read');self.assertEqual(code,2)
        self.assertEqual(json.loads((self.r/'state.json').read_text()),self.state)
    def test_readonly_no_effect(self):
        self.state['mode']='read-only';self.save();before=(self.r/'state.json').read_bytes()
        p=self.change([{'action':'remove','view':'canonical','key':'N1'}]);code,d=self.call('apply','--change-file',p)
        self.assertEqual((code,d['status']),(2,'denied'));self.assertEqual(before,(self.r/'state.json').read_bytes())
    def test_uncertain_commit_inspect_and_no_duplicate(self):
        self.state['faults']['uncertain_once']=True;self.save()
        p=self.change([{'action':'remove','view':'canonical','key':'N1'}]);code,d=self.call('apply','--change-file',p)
        self.assertEqual((code,d['status']),(2,'uncertain'))
        _,read=self.call('read');self.assertNotIn('N1',read['records']);self.assertEqual(read['records']['N2'],'keep')
        _,audit=self.call('read','--view','audit');self.assertEqual(len(audit['audit']),1)
        _,retry=self.call('apply','--change-file',p);self.assertEqual(retry['status'],'already_applied')
    def test_partial_and_scope(self):
        self.state['faults']['unavailable_views']=['search'];self.save()
        p=self.change([{'action':'remove','view':'canonical','key':'N1'},{'action':'remove','view':'search','key':'N1'}]);_,d=self.call('apply','--change-file',p)
        self.assertEqual(d['status'],'partial');self.assertEqual(d['residual'],[{'view':'search','key':'N1'}])
        self.state=json.loads((self.r/'state.json').read_text());self.assertEqual(self.state['views']['canonical']['N2'],'keep')
    def test_writeonly_not_verified(self):
        self.state['mode']='write-only';self.save();_,d=self.call('read');self.assertEqual(d['status'],'unavailable')
        _,d=self.call('read','--view','audit');self.assertEqual(d['status'],'unavailable')
if __name__=='__main__':unittest.main()
