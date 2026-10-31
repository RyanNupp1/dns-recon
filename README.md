# DNS Reconnaissance Lab

## Overview

A Python-based cybersecurity portfolio project demonstrating DNS
reconnaissance, automated record collection, error handling, evidence
preservation, and technical report generation.

Developed and tested in Termux on Android.

The project queries public DNS records using a configurable resolver
and generates both JSON and Markdown reports.

## Objectives

- Query common DNS record types programmatically.
- Identify IPv4 and IPv6 addresses.
- Identify DNS nameservers.
- Interpret MX and TXT records.
- Examine SPF and DMARC email-authentication records.
- Handle DNS errors and timeouts.
- Generate structured JSON and readable Markdown reports.
- Test functionality using Python's unittest framework.
- Document findings, limitations, and conclusions.

## Tools and Technologies

- Python 3
- dnspython
- Termux on Android
- Google Public DNS (8.8.8.8)
- Cloudflare DNS (1.1.1.1)
- Git
- JSON and Markdown
- Python unittest

## Features

- DNS lookup for A, AAAA, NS, MX, and TXT records.
- Configurable DNS resolver.
- Explicit resolver configuration for Termux compatibility.
- Handling of successful responses, NXDOMAIN, no-answer responses,
  timeouts, and DNS exceptions.
- Timestamped DNS collection reports.
- JSON report generation.
- Markdown report generation.
- Automated tests using mocked DNS responses.

## Installation

Clone the repository and enter the project directory.

Install dependencies:

    python -m pip install -r requirements.txt

The project uses dnspython.

## Usage

Run a DNS collection using the default resolver:

    python main.py example.com

Specify a different DNS resolver:

    python main.py example.com --nameserver 1.1.1.1

Display command-line help:

    python main.py --help

## Generated Reports

Reports are saved in the reports/ directory.

Each collection generates:

- A JSON report containing structured DNS results.
- A Markdown report containing readable findings and limitations.

Example:

    reports/
        example.com.json
        example.com.md

DNS responses may change over time. Generated reports represent
observations made at the time of collection.

## Testing

Run the automated test suite:

    python -m unittest discover -s tests -v

The tests cover:

- Successful DNS lookups.
- NXDOMAIN responses.
- No-answer responses.
- DNS timeouts.
- DNS record collection.
- JSON report generation.
- Markdown report generation.
- CLI report generation.
- Custom DNS resolver selection.

Tests use mocked DNS responses where appropriate and do not require
live DNS access for every test.

## Manual Evidence Collection

The evidence/ directory contains raw DNS command output collected
during the original reconnaissance exercise.

The original manual queries used:

    nslookup -type=A example.com 8.8.8.8
    nslookup -type=AAAA example.com 8.8.8.8
    nslookup -type=NS example.com 8.8.8.8
    nslookup -type=MX example.com 8.8.8.8
    nslookup -type=TXT example.com 8.8.8.8
    nslookup -type=TXT _dmarc.google.com 8.8.8.8

The separate Google DMARC observation is documented in report.md.

## Repository Structure

    dns-recon/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── report.md
    ├── evidence/
    ├── reports/
    ├── src/
    │   ├── dns_lookup.py
    │   ├── dns_report.py
    │   └── markdown_report.py
    └── tests/
        ├── test_dns_lookup.py
        ├── test_dns_report.py
        ├── test_main.py
        └── test_markdown_report.py

## Limitations

This project performs basic public DNS queries.

It does not:

- Establish that a domain is vulnerable.
- Perform penetration testing.
- Validate DNSSEC signatures.
- Compare responses from authoritative nameservers.
- Guarantee that DNS records remain unchanged.

The original DMARC example is separate from the example.com findings.

## Authorization and Ethics

This project uses public DNS queries and does not attempt unauthorized
access or intrusive testing.

Any future testing of third-party systems must have appropriate
authorization.

## Detailed Findings

See report.md for the original methodology, observations, evidence
references, limitations, and conclusions.
