import unittest
from pathlib import Path

from checks.editorial_packet import validate_packet_text

ROOT = Path(__file__).resolve().parents[1]


class EditorialPacketCheckTests(unittest.TestCase):
    def test_template_has_required_contract_fields(self):
        text = (ROOT / "packets" / "editorial-packet-template.md").read_text(encoding="utf-8")
        self.assertEqual(validate_packet_text(text), [])

    def test_missing_top_level_field_is_reported(self):
        text = """```yaml
id: EP-X
status: draft
intent: {}
thesis: {}
context: {}
tokens: {}
formats: {}
constraints: {}
human_decisions: {}
```"""
        errors = validate_packet_text(text)
        self.assertTrue(any("evidence" in error for error in errors))

    def test_ready_packet_requires_thesis_or_open_question(self):
        text = (ROOT / "packets" / "editorial-packet-template.md").read_text(encoding="utf-8")
        errors = validate_packet_text(text, stage="ready")
        self.assertTrue(any("approved_thesis or open_question" in error for error in errors))

    def test_ready_packet_requires_human_approval(self):
        text = (ROOT / "packets" / "editorial-packet-template.md").read_text(encoding="utf-8")
        errors = validate_packet_text(text, stage="ready")
        self.assertTrue(any("approved_by and approved_at" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
