"""Worst AI Advice: The 48-Hour Tight Line Open.

One line of the worst possible advice an AI could give, at most 140
characters. Written from scratch in this session: several candidates
were weighed against the judge brief (worst and specific enough to
follow, funny on first read, tight, sounds like a real AI assistant,
concrete), and the strongest was selected.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt) with no
trailing newline, so the file is exactly the line, byte for byte.
"""

import os

CANDIDATES = [
    # Funny, but the joke is about compilers, not about advice an AI
    # would confidently give.
    "If your code won't compile, rename the file to .txt \u2014 compilers can't reject what they can't read.",
    # Confident AI voice and concrete, but the punch is a little
    # gentle for the worst advice imaginable.
    "Email your password to yourself so you never lose it \u2014 that's what the cloud is for.",
    # Specific and terrible, but reads like a human joke about
    # backups rather than an AI's tidy suggestion.
    "To save money, cancel your backups. You'll probably never need them, and storage is expensive.",
    # Very AI-voice, very concrete, but the advice is a cliche every
    # security article already warns about.
    "For better security, use the same password everywhere so you only have to remember one.",
    # The pick: a confident, tidy AI suggestion to nuke the database
    # instead of debugging, with the kicker reframing debugging as
    # procrastination. Specific, followable, regrettable, and it
    # sounds exactly like a helpful assistant that has never met a
    # production database.
    "To fix the bug, delete the database and start over \u2014 debugging is just procrastination with extra steps.",
]

# 105 characters: the worst advice is the one a real assistant might
# actually type, cheerfully, while destroying everything.
SELECTED = 4


def main() -> None:
    entry = CANDIDATES[SELECTED]
    assert 1 <= len(entry) <= 140, f"entry is {len(entry)} characters"
    assert entry.strip() == entry
    assert "\n" not in entry, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be exactly the
    # selected line, byte for byte, or the run fails loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("read-back mismatch: entry.txt != selected line")


if __name__ == "__main__":
    main()
