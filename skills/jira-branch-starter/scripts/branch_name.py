#!/usr/bin/env python3
"""Build a Jira-based git branch name and optionally create it."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata


VALID_KINDS = {"feature", "fix"}


def slugify(text: str, issue_key: str | None = None, max_length: int = 48) -> str:
    value = text.strip()
    if issue_key:
        value = re.sub(re.escape(issue_key), " ", value, flags=re.IGNORECASE)

    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")

    if max_length > 0 and len(value) > max_length:
        value = value[:max_length].rstrip("-")

    return value


def build_branch_name(kind: str, issue_key: str, summary: str, max_length: int = 48) -> str:
    if kind not in VALID_KINDS:
        raise ValueError(f"kind must be one of: {', '.join(sorted(VALID_KINDS))}")

    slug = slugify(summary, issue_key=issue_key, max_length=max_length)
    return f"{kind}/{issue_key}" if not slug else f"{kind}/{issue_key}-{slug}"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Jira-based branch name and optionally create it."
    )
    parser.add_argument("--kind", required=True, choices=sorted(VALID_KINDS))
    parser.add_argument("--issue-key", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument(
        "--max-slug-length",
        type=int,
        default=48,
        help="Maximum slug length after normalization.",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create the branch locally with git switch -c.",
    )
    parser.add_argument(
        "--base",
        default=None,
        help="Optional base branch ref to pass to git switch -c.",
    )
    return parser.parse_args(argv)


def create_branch(branch_name: str, base: str | None) -> None:
    cmd = ["git", "switch", "-c", branch_name]
    if base:
        cmd.append(base)
    subprocess.run(cmd, check=True)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    branch_name = build_branch_name(
        args.kind,
        args.issue_key,
        args.summary,
        max_length=args.max_slug_length,
    )

    if args.create:
        create_branch(branch_name, args.base)
    else:
        print(branch_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
