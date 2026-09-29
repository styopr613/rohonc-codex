import unittest

import ktrefs


class EvidenceFoliosTest(unittest.TestCase):
    def test_supported_reference_forms(self):
        text = "at 033v05, 074v:1, 013vc1:03, 154vp1:01 and (204r)"
        self.assertEqual(
            ktrefs.evidence_folios(text),
            {"013v", "033v", "074v", "154v", "204r"},
        )

    def test_does_not_start_inside_an_alphanumeric_token(self):
        self.assertEqual(ktrefs.evidence_folios("x033v05 2015r07"), set())

    def test_optional_document_validation(self):
        self.assertEqual(
            ktrefs.evidence_folios("033v05 and 999r01", {"033v"}),
            {"033v"},
        )


if __name__ == "__main__":
    unittest.main()
