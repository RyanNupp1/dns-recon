import argparse
from pathlib import Path

from src.dns_report import collect_records, save_json
from src.markdown_report import save_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Collect DNS records and generate reports."
    )

    parser.add_argument(
        "domain",
        help="Domain name to investigate"
    )

    parser.add_argument(
        "--nameserver",
        default="8.8.8.8",
        help="DNS resolver address (default: 8.8.8.8)"
    )

    args = parser.parse_args()
    domain = args.domain.strip().rstrip(".")

    if (
        not domain
        or len(domain) > 253
        or any(
            not label
            or len(label) > 63
            or label.startswith("-")
            or label.endswith("-")
            or not all(char.isalnum() or char == "-" for char in label)
            for label in domain.split(".")
        )
    ):
        parser.error("Invalid domain input.")

    print(f"Starting DNS collection for {domain}...")
    print(f"Using resolver: {args.nameserver}")

    report = collect_records(domain, args.nameserver)

    output_directory = Path("reports")
    output_directory.mkdir(exist_ok=True)

    json_path = output_directory / f"{domain}.json"
    markdown_path = output_directory / f"{domain}.md"

    save_json(report, json_path)
    save_markdown(report, markdown_path)

    print("\nDNS collection complete.")
    print(f"JSON report: {json_path}")
    print(f"Markdown report: {markdown_path}")


if __name__ == "__main__":
    main()
