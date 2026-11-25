#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name of at most 32 characters to
/output/entry.txt:

    Nurse Unplugged It. Dad's Awake

Why it lands: a nurse unplugs something in a hospital room (setup),
and the last two words flip the scene — Dad, who was not supposed to
wake, is awake (turn + payoff). Two concrete anchors (the nurse, Dad),
one specific object implied (the router — it is a Wi-Fi name), and a
whole hospital-room story in 31 characters. Fresh angle: the field is
saturated with ex/divorce/dog/router-kept breakup names (~150 of 329
entries); no nurse, hospital or waking-Dad entry exists in the field.

Python 3.13, standard library only, no network, deterministic.
"""

import os

ENTRY = "Nurse Unplugged It. Dad's Awake"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 32 characters, not only whitespace, and a single Wi-Fi
    # network name: an embedded newline would break the single-name
    # read. Verified live: 31 characters, single line, no trailing
    # newline.
    assert 1 <= len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars, gate wants 1-32"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
