#!/usr/bin/env python3
"""Protect named files from edits by Claude Code and Codex."""

import json
import sys
from collections.abc import Iterator
from pathlib import Path

PROTECTED_NAMES = {"references.bib", "settings.json"}
PATCH_HEADERS = ("*** Add File: ", "*** Delete File: ", "*** Update File: ")


def patch_paths(patch: str) -> Iterator[str]:
    """Yield file-operation paths, including the destination of a rename."""
    if not isinstance(patch, str):
        raise ValueError("expected a patch string")

    in_update = False
    for line in patch.split("\n"):
        # A leading space is file content inside an update, but legal
        # indentation for a header following an add or delete.
        header = line.rstrip() if in_update else line.strip()
        if header.startswith(PATCH_HEADERS):
            in_update = header.startswith("*** Update File: ")
            yield header.partition(": ")[2]
        elif in_update and header.startswith("*** Move to: "):
            yield header.removeprefix("*** Move to: ")


def main() -> int:
    """Return the PreToolUse exit code for the JSON event on stdin."""
    try:
        event = json.load(sys.stdin)
        tool = event["tool_name"]
        if tool in ("Edit", "Write"):
            paths = (event["tool_input"]["file_path"],)
        elif tool == "apply_patch":
            paths = patch_paths(event["tool_input"]["command"])
        else:
            return 0

        for path in paths:
            if Path(path).name in PROTECTED_NAMES:
                print(f"Protected file: {path}. Edit it manually.", file=sys.stderr)
                return 2
    except (KeyError, TypeError, ValueError):
        print("File protection could not read the edit request.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
