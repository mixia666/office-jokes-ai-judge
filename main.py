#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

Writes one one-line office joke to /output/entry.txt, where the
competition's sealed scorer checks it and the AI judge reads it.
The program is deterministic: every run writes the same line.
"""

import os
import sys

# Jokes drafted for this entry. Exactly one of them is submitted:
# the one named by ENTRY below. The reply-all line won the pick: it
# is a real joke (not an observation), everyone who has ever worked
# in an office has lived it, and it turns at the very end, where the
# punishment for the pile-on is the most office sentence there is.
CANDIDATES = [
    "I hit reply-all to tell 400 people to stop replying all. All 400 replied-all to agree \u2014 and now it's a recurring meeting.",
    "Our Monday meeting exists to plan the week's meetings, and the plan is always the same: more meetings, but with slides.",
    "The office printer only jams when the CEO prints. Even the machines here have learned to manage up.",
    "Our printer has printed more resignation letters than reports. It is the only thing in this office with a clear career path.",
]

ENTRY = CANDIDATES[0]

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
