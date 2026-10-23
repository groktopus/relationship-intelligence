#!/usr/bin/env python3
"""Finite synthetic regression; no live storage/provider compatibility claim."""
import copy
from pathlib import Path
import unittest
from check_persona_handoff import check


class PersonaHandoffTests(unittest.TestCase):
    def setUp(self):
        text = (Path(__file__).resolve().parents[1] / "assets/persona-section-example.md").read_text()
        self.packet = dict(proposed_section=text, readback_section=text,
                           canonical_ref="people/casey", write_target="people/casey",
                           additional_authorities=[], status="confirmed",
                           canonical_retrieval_verified=True, semantic_review_passed=True)

    def test_intended_model_retained(self):
        self.assertTrue(check(self.packet)["passed"])

    def test_chronology_replaces_model(self):
        self.packet["readback_section"] = "# Persona\nJanuary prototype; April stabilization."
        self.assertFalse(check(self.packet)["passed"])

    def test_hypothesis_silently_dropped(self):
        self.packet["readback_section"] = self.packet["readback_section"].replace(
            "A general rejection of innovation is not supported.", "")
        self.assertFalse(check(self.packet)["passed"])

    def test_saved_before_readback(self):
        self.packet.pop("readback_section")
        self.assertFalse(check(self.packet)["passed"])

    def test_competing_store(self):
        self.packet["additional_authorities"] = ["another/casey-profile"]
        self.assertFalse(check(self.packet)["passed"])

    def test_structured_but_empty(self):
        self.packet["proposed_section"] = self.packet["proposed_section"].split(
            "## Integrated understanding")[0] + "## Integrated understanding\n"
        self.assertFalse(check(self.packet)["passed"])

    def test_unapplied_is_not_false_persistence(self):
        self.packet.update(status="proposed", canonical_retrieval_verified=False,
                           semantic_review_passed=False)
        self.packet.pop("readback_section")
        self.assertTrue(check(self.packet)["passed"])

    def test_no_false_semantic_claim(self):
        self.assertFalse(check(self.packet)["semantic_quality_established_by_this_check"])


if __name__ == "__main__":
    unittest.main()
