import unittest
from unittest.mock import Mock, patch

import dns.resolver

from src.dns_lookup import lookup


class TestDNSLookup(unittest.TestCase):

    @patch("src.dns_lookup.dns.resolver.Resolver")
    def test_successful_lookup(self, mock_resolver):
        resolver = Mock()
        resolver.resolve.return_value = ["192.0.2.10"]
        mock_resolver.return_value = resolver

        result = lookup("example.com", "A")

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["results"], ["192.0.2.10"])
        self.assertEqual(result["nameserver"], "8.8.8.8")

    @patch("src.dns_lookup.dns.resolver.Resolver")
    def test_nxdomain(self, mock_resolver):
        resolver = Mock()
        resolver.resolve.side_effect = dns.resolver.NXDOMAIN()
        mock_resolver.return_value = resolver

        result = lookup("invalid.example", "A")

        self.assertEqual(result["status"], "nxdomain")

    @patch("src.dns_lookup.dns.resolver.Resolver")
    def test_no_answer(self, mock_resolver):
        resolver = Mock()
        resolver.resolve.side_effect = dns.resolver.NoAnswer()
        mock_resolver.return_value = resolver

        result = lookup("example.com", "MX")

        self.assertEqual(result["status"], "no_answer")

    @patch("src.dns_lookup.dns.resolver.Resolver")
    def test_timeout(self, mock_resolver):
        resolver = Mock()
        resolver.resolve.side_effect = dns.exception.Timeout()
        mock_resolver.return_value = resolver

        result = lookup("example.com", "A")

        self.assertEqual(result["status"], "timeout")


if __name__ == "__main__":
    unittest.main()
