# DNS Reconnaissance Report

## 1. Objective

Collect and interpret selected DNS records to practice basic reconnaissance, evidence preservation, and technical reporting.

## 2. Scope

- Primary domain: example.com
- Separate DMARC example: _dmarc.google.com
- DNS resolver: 8.8.8.8 (Google Public DNS)
- Environment: Termux on Android
- Method: nslookup DNS queries
- Authorization: Public DNS lookups only; no intrusive testing performed

## 3. Methodology

Queries were performed for A, AAAA, NS, MX, and TXT records for example.com. A separate TXT query was performed for Google's DMARC record.

Raw command output was saved under the evidence/ directory.

## 4. Findings

4.1 A Records

Observed IPv4 addresses:

- 104.20.23.154
- 172.66.147.243

Interpretation: The domain resolved to two IPv4 addresses at the time of testing. The reason for multiple addresses cannot be established from this query alone.

Evidence: evidence/a-records.txt

4.2 AAAA Records

Observed IPv6 addresses:

- 2606:4700:10::6814:179a
- 2606:4700:10::ac42:93f3

Interpretation: IPv6 addresses were published in DNS. This does not independently confirm end-to-end IPv6 connectivity.

Evidence: evidence/aaaa-records.txt

4.3 NS Records

Observed nameservers:

- elliott.ns.cloudflare.com
- hera.ns.cloudflare.com

Interpretation: The domain's DNS delegation identifies Cloudflare nameservers.

Evidence: evidence/ns-records.txt

4.4 MX Record

Observed record:

- 0 . (Null MX)

Interpretation: The domain explicitly indicates that it does not accept email. This is not, by itself, a security finding.

Evidence: evidence/mx-records.txt

4.5 TXT Records

Observed strings:

- v=spf1 -all
- _k2n1y4vw3qtb4skdx9e7dxt97qrmmq9

Interpretation: The SPF policy authorizes no sending hosts for this domain. The purpose of the second string was not determined during this exercise.

Evidence: evidence/txt-records.txt

4.6 DMARC Record — Separate Domain

Queried name: _dmarc.google.com

Observed policy:

v=DMARC1; p=reject; rua=mailto:mailauth-reports@google.com

Interpretation: The policy requests rejection of messages that fail DMARC evaluation. The rua tag specifies an aggregate-report destination. This finding applies to the queried Google domain, not to example.com.

Evidence: evidence/dmarc-google.txt

## 5. Security Assessment

The queries demonstrate how public DNS records can reveal addressing, DNS hosting, and email-handling policies.

No vulnerability was established by these DNS lookups. Public DNS records are intended to be discoverable, and the presence of multiple IP addresses or a particular DNS provider is not inherently a security weakness.

## 6. Limitations

- Results represent DNS responses at the time of collection.
- DNS records may change.
- No authoritative-server comparison, DNSSEC validation, or active vulnerability testing was performed.
- The second TXT string's purpose was not established.
- Google's DMARC record was examined separately from example.com.

## 7. Evidence Inventory

- evidence/a-records.txt
- evidence/aaaa-records.txt
- evidence/ns-records.txt
- evidence/mx-records.txt
- evidence/txt-records.txt
- evidence/dmarc-google.txt

## 8. Conclusion

This exercise demonstrated basic DNS reconnaissance, structured evidence collection, interpretation of common record types, and the documentation of limitations. It provides a foundation for further work in DNS security, networking, and security reporting.
