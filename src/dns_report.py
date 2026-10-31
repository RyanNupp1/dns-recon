import json
from datetime import datetime, timezone
from pathlib import Path

from src.dns_lookup import lookup


RECORD_TYPES = ["A", "AAAA", "NS", "MX", "TXT"]


def collect_records(domain, nameserver="8.8.8.8"):
    report = {
        "domain": domain,
        "nameserver": nameserver,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "records": {},
    }

    for record_type in RECORD_TYPES:
        report["records"][record_type] = lookup(
            domain,
            record_type,
            nameserver,
        )

    return report


def save_json(report, output_path):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return path
