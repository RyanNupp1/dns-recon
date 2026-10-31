import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.dns_report import collect_records, save_json


class TestDNSReport(unittest.TestCase):

    @patch("src.dns_report.lookup")
    def test_collect_records(self, mock_lookup):
        mock_lookup.side_effect = lambda domain, record_type, nameserver: {
            "domain": domain,
            "record_type": record_type,
            "nameserver": nameserver,
            "results": [],
            "status": "success",
        }

        report = collect_records("example.com")

        self.assertEqual(report["domain"], "example.com")
        self.assertEqual(report["nameserver"], "8.8.8.8")
        self.assertIn("collected_at", report)
        self.assertEqual(
            set(report["records"]),
            {"A", "AAAA", "NS", "MX", "TXT"},
        )
        self.assertEqual(mock_lookup.call_count, 5)

    def test_save_json(self):
        report = {
            "domain": "example.com",
            "records": {"A": {"status": "success"}},
        }

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "reports" / "test.json"

            saved_path = save_json(report, output)

            self.assertTrue(saved_path.exists())

            with saved_path.open(encoding="utf-8") as file:
                loaded = json.load(file)

            self.assertEqual(loaded, report)


if __name__ == "__main__":
    unittest.main()
