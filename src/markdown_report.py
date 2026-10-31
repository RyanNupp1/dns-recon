from pathlib import Path


def generate_markdown(report):
    lines = [
        f"# DNS Reconnaissance Report: {report['domain']}",
        "",
        f"- **Resolver:** {report['nameserver']}",
        f"- **Collected at (UTC):** {report['collected_at']}",
        "",
        "## DNS Record Findings",
    ]

    for record_type, result in report["records"].items():
        lines.extend([
            "",
            f"### {record_type}",
            f"- **Status:** {result['status']}",
        ])

        if result.get("results"):
            lines.append("- **Results:**")
            for answer in result["results"]:
                lines.append(f"  - `{answer}`")
        else:
            lines.append("- No results returned.")

        if result.get("error"):
            lines.append(f"- **Error:** {result['error']}")

    lines.extend([
        "",
        "## Scope and Limitations",
        "",
        "- This report records DNS responses from the specified resolver.",
        "- DNS records may change over time.",
        "- Results alone do not establish that a domain is vulnerable.",
        "- This report does not perform DNSSEC validation or penetration testing.",
        "",
    ])

    return "\n".join(lines)


def save_markdown(report, output_path):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(generate_markdown(report), encoding="utf-8")
    return path
