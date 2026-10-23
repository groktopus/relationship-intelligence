"""Fixture integrity only. Does not judge semantic quality or actual model behavior."""
import json
from pathlib import Path
import unittest

class Fixtures(unittest.TestCase):
    def test_cases_and_support(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'evals/persona-semantic-quality.json').read_text())
        self.assertEqual(len(data['cases']),7)
        self.assertEqual(len({c['id'] for c in data['cases']}),7)
        for case in data['cases']:
            self.assertIn(case['source_set'],data['sources'])
            self.assertIn(case['expected'],['PASS','FAIL','PARTIAL'])
            self.assertTrue(case['reasons'])
            self.assertTrue(case['candidate'])
        self.assertEqual(data['sources']['rich'][-1]['duplicate_of'],'G2')
    def test_intended_contrasts(self):
        cases={c['id']:c for c in json.loads((Path(__file__).resolve().parents[1]/'evals/persona-semantic-quality.json').read_text())['cases']}
        self.assertEqual(cases['rich-skeletal']['expected'],'FAIL')
        self.assertEqual(cases['rich-grounded']['expected'],'PASS')
        self.assertEqual(cases['sparse-bounded']['expected'],'PASS')
        self.assertEqual(cases['sparse-padded']['expected'],'FAIL')
        self.assertEqual(cases['template-only']['expected'],'FAIL')
        self.assertEqual(cases['rich-unperformed']['expected'],'PARTIAL')
        self.assertEqual(cases['rich-pooled-confidence']['expected'],'FAIL')

if __name__=='__main__':unittest.main()
