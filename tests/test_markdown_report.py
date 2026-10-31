import unittest

from src.markdown_report import generate_markdown


class TestMarkdownReport(unittest.TestCase):

    def setUp(self):
        self.report = {
            "domain": "example.com",
            "nameserver": "8.8.8.8",
            "collected_at": "2026-10-30T15:10:46+00:00",
            "records": {
                "A": {
                    "status": "success",
                    "results": ["192.0.2.10"],
                },
                "MX": {
                    "status": "success",
                    "results": ["0 ."],
                },
                "TXT": {
                    "status": "success",
                    "results": ['"v=spf1 -all"'],
                },
            },
        }

    def test_report_contains_domain_and_resolver(self):
        output = generate_markdown(self.report)

        self.assertIn("# DNS Reconnaissance Report: example.com", output)
        self.assertIn("8.8.8.8", output)

    def test_report_contains_record_results(self):
        output = generate_markdown(self.report)

        self.assertIn("192.0.2.10", output)
        self.assertIn("0 .", output)
        self.assertIn("v=spf1 -all", output)

    def test_report_contains_scope_limitations(self):
        output = generate_markdown(self.report)

        self.assertIn("DNSSEC validation", output)
        self.assertIn("do not establish", output)


if __name__ == "__main__":
    unittest.main()
