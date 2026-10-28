# DNS Reconnaissance Lab

## Overview

A beginner cybersecurity portfolio project demonstrating DNS reconnaissance, evidence collection, interpretation of DNS records, and technical report writing using Termux on Android.

The lab uses "example.com" for general DNS queries and separately examines the DMARC TXT record published by "google.com".

## Objectives

- Query common DNS record types using "nslookup".
- Identify IPv4 and IPv6 addresses.
- Identify DNS nameservers.
- Interpret MX and TXT records.
- Examine SPF and DMARC email-authentication policies.
- Preserve raw command output as evidence.
- Document findings, limitations, and conclusions in Markdown.

## Tools and Environment

- Android with Termux
- "nslookup"
- Google Public DNS ("8.8.8.8")
- Markdown
- Git for version control

## Methodology

The lab queries the following DNS record types:

| Record | Purpose |
| A | IPv4 address records |
| AAAA | IPv6 address records |
| NS | DNS nameservers |
| MX | Mail exchange records |
| TXT | Text records, including SPF policy |
| DMARC TXT | Email-authentication policy at `_dmarc.google.com` |

Raw responses are saved in "evidence/", and their interpretations are documented in "report.md".

## Repository Structure

dns-recon/
├── README.md
├── report.md
└── evidence/
    ├── a-records.txt
    ├── aaaa-records.txt
    ├── ns-records.txt
    ├── mx-records.txt
    ├── txt-records.txt
    └── dmarc-google.txt

## Reproducing the Lab

Install the required DNS utility in Termux if it is not already available:

pkg install dnsutils

Run the queries from the project directory:

nslookup -type=A example.com 8.8.8.8
nslookup -type=AAAA example.com 8.8.8.8
nslookup -type=NS example.com 8.8.8.8
nslookup -type=MX example.com 8.8.8.8
nslookup -type=TXT example.com 8.8.8.8
nslookup -type=TXT _dmarc.google.com 8.8.8.8

DNS responses may change over time. The included evidence files represent the results collected during this lab.

## Key Learning Outcomes

- Distinguished IPv4 and IPv6 DNS records.
- Identified nameserver delegation.
- Recognized a Null MX record.
- Interpreted an SPF policy ending in "-all".
- Examined a DMARC policy using "p=reject".
- Practiced preserving command output and writing evidence-based conclusions.

## Limitations

This project performs basic public DNS queries only. It does not establish that a domain is vulnerable, validate DNSSEC, or perform an active penetration test.

The DMARC example is separate from the "example.com" findings.

## Authorization and Ethics

This exercise uses public DNS queries and does not attempt unauthorized access or intrusive testing. Any future testing of third-party systems must have appropriate authorization.

## Detailed Report

See "report.md" (report.md) for the methodology, findings, evidence references, limitations, and conclusion.
