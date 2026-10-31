import unittest
from unittest.mock import patch
from pathlib import Path
import tempfile

from main import main


class TestMain(unittest.TestCase):

    @patch("main.save_markdown")
    @patch("main.save_json")
    @patch("main.collect_records")
    @patch("sys.argv", ["main.py", "example.com"])
    def test_main_generates_reports(
        self,
        mock_collect,
        mock_json,
        mock_markdown,
    ):
        mock_collect.return_value = {
            "domain": "example.com",
            "nameserver": "8.8.8.8",
            "collected_at": "2026-10-31T00:00:00+00:00",
            "records": {},
        }

        main()

        mock_collect.assert_called_once_with("example.com", "8.8.8.8")
        mock_json.assert_called_once()
        mock_markdown.assert_called_once()

    @patch("sys.argv", ["main.py", "example.com", "--nameserver", "1.1.1.1"])
    @patch("main.collect_records")
    @patch("main.save_json")
    @patch("main.save_markdown")
    def test_custom_nameserver(
        self,
        mock_markdown,
        mock_json,
        mock_collect,
    ):
        mock_collect.return_value = {
            "domain": "example.com",
            "nameserver": "1.1.1.1",
            "collected_at": "2026-10-31T00:00:00+00:00",
            "records": {},
        }

        main()

        mock_collect.assert_called_once_with("example.com", "1.1.1.1")


if __name__ == "__main__":
    unittest.main()
    @patch("main.collect_records")
    @patch("sys.argv", ["main.py", "../unsafe"])
    def test_rejects_invalid_domain(self, mock_collect):
        with self.assertRaises(SystemExit):
            main()

        mock_collect.assert_not_called()
