#!/usr/bin/env python3
"""Offline structure/content-retention check, not a semantic or live-store validator.

Usage: python3 scripts/check_persona_handoff.py packet.json
Packet: proposed_section, optional readback_section, canonical_ref, write_target,
additional_authorities (list), status. All text is supplied; no network/store IO.
"""
import json
import re
import sys

HEADINGS = ["Integrated understanding", "Evidence and temporal scope",
            "Confidence and alternatives", "Communication implications",
            "Adaptive questions and model updates"]


def check(packet):
    errors = []
    proposed = packet.get("proposed_section", "")
    if re.findall(r"^# .+$", proposed, re.M) != ["# Persona"]:
        errors.append("Expected one H1 Persona in the managed section")
    if re.findall(r"^## (.+)$", proposed, re.M) != HEADINGS:
        errors.append("Persona H2 sections missing, repeated or out of order")
    intro = proposed.split("## ", 1)[0]
    if not all(x in intro for x in ["Relationship Intelligence", "1.0.0",
                                   "references/persona-output-contract.md"]):
        errors.append("Missing named skill/update attribution or contract version")
    chunks = re.split(r"^## .+$", proposed, flags=re.M)[1:]
    if any(not x.strip() for x in chunks):
        errors.append("Empty section; provide supported content or a specific unknown")
    canonical = packet.get("canonical_ref")
    if not canonical or packet.get("write_target") != canonical:
        errors.append("Missing or conflicting canonical write target")
    if packet.get("additional_authorities"):
        errors.append("Competing authoritative persona stores")
    if packet.get("status") == "confirmed":
        readback = packet.get("readback_section")
        if readback is None:
            errors.append("Confirmed status without canonical readback")
        elif readback != proposed:
            errors.append("Readback differs from intended reconciled persona; inspect content loss/revision")
        if not packet.get("canonical_retrieval_verified"):
            errors.append("Confirmed status without retrieval verification")
        if not packet.get("semantic_review_passed"):
            errors.append("Confirmed status without substantive model review")
    return {"kind": "offline_supplied_evidence_only", "passed": not errors,
            "errors": errors, "semantic_quality_established_by_this_check": False}


if __name__ == "__main__":
    result = check(json.load(open(sys.argv[1], encoding="utf-8")))
    print(json.dumps(result, indent=2))
    sys.exit(not result["passed"])
