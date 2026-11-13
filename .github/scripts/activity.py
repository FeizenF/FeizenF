"""Append one dated line to activity.log and refresh the README sync stamp.

The script is idempotent per UTC day: a second run only refreshes the README
timestamp, so the workflow can be scheduled twice a day as a retry without
producing duplicate entries.
"""
from __future__ import annotations

import datetime as dt
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOG = ROOT / "activity.log"
README = ROOT / "README.md"

HEADER = [
    "# Activity log",
    "",
    "A short daily entry, written by `.github/workflows/activity.yml`.",
]

TOPICS = [
    "cyber security",
    "digital forensics",
    "web development",
    "mobile development",
    "systems study",
]

MAX_ENTRIES = 365
ENTRY_RE = re.compile(r"^- \d{4}-\d{2}-\d{2}T")
SYNC_RE = re.compile(r"^\d{4}-\d{2}-\d{2} · last sync .*$")


def update_log(now: dt.datetime) -> None:
    day = now.strftime("%Y-%m-%d")
    lines = LOG.read_text(encoding="utf-8").splitlines() if LOG.exists() else []
    entries = [line for line in lines if ENTRY_RE.match(line)]

    if not any(line.startswith(f"- {day}") for line in entries):
        topic = TOPICS[now.timetuple().tm_yday % len(TOPICS)]
        stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        entries.append(f"- {stamp} · {topic} · status: online")

    entries = entries[-MAX_ENTRIES:]
    LOG.write_text("\n".join([*HEADER, *entries]) + "\n", encoding="utf-8")


def update_readme(now: dt.datetime) -> None:
    if not README.exists():
        return

    stamp = f"{now.strftime('%Y-%m-%d')} · last sync {now.strftime('%H:%M')} UTC"
    text = README.read_text(encoding="utf-8")
    text = SYNC_RE.sub(stamp, text, count=1)
    README.write_text(text, encoding="utf-8")


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc)
    update_log(now)
    update_readme(now)


if __name__ == "__main__":
    main()
