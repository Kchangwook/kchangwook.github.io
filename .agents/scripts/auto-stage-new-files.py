#!/usr/bin/env python3
"""PostToolUse hook: automatically `git add` newly created untracked files in this workspace."""

import json
import os
import subprocess
import sys


def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        print("{}")
        return

    if data.get("error"):
        print("{}")
        return

    args = (data.get("toolCall") or {}).get("args") or {}
    target = args.get("Path") or args.get("TargetFile") or args.get("path")
    if not target or not isinstance(target, str):
        print("{}")
        return

    repo_root = os.path.realpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    )
    abs_target = os.path.realpath(
        target if os.path.isabs(target) else os.path.join(repo_root, target)
    )

    try:
        if os.path.commonpath([repo_root, abs_target]) != repo_root:
            print("{}")
            return
    except ValueError:
        print("{}")
        return

    if not os.path.isfile(abs_target):
        print("{}")
        return

    rel_path = os.path.relpath(abs_target, repo_root)
    if rel_path == ".git" or rel_path.startswith(".git" + os.sep):
        print("{}")
        return

    # Skip gitignored files
    ignored = subprocess.run(
        ["git", "-C", repo_root, "check-ignore", "-q", "--", rel_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if ignored.returncode == 0:
        print("{}")
        return

    # Only stage newly created (untracked) files; leave modifications to tracked files unstaged
    tracked = subprocess.run(
        ["git", "-C", repo_root, "ls-files", "--error-unmatch", "--", rel_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if tracked.returncode == 0:
        print("{}")
        return

    subprocess.run(
        ["git", "-C", repo_root, "add", "--", rel_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("{}")


if __name__ == "__main__":
    main()
