"""The Tired Dark Lord: A 100-Word Villain Monologue.

Deterministically writes ONE monologue (a fixed constant, no network,
no randomness, no runtime reads) as a single line, UTF-8, no trailing
newline, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Winner: Candidate 7 (the Tithe-Demon of Hell) — 97 words, 494 chars.
See CANDIDATES.md for the eight drafts and the judging.
"""

import os

TEXT = 'Sign here. The tithe is due, and Hell keeps books. Your soul is item seven on page... four hundred and twelve? No. Four hundred and twenty. The ink is still wet. I have stamped ten thousand souls this week, and each one bleeds the same small red seal. Yours is no different. Your name. It is... it is on the tip of my tongue. It starts with a... a letter. It always starts with a letter. Pay the tithe, keep the receipt, and go. The line behind you is long, and the line, unlike me, never ends.'

MAX_CHARS = 600


def validate(text):
    """Gate: the sealed scorer's rules. Raises ValueError on rejection."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    return True


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    validate(TEXT)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read-back gate: re-read the file and assert it is byte-identical
    # to TEXT and still passes the gate (UTF-8, 1-600 chars, one line,
    # no trailing newline).
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == TEXT, "entry.txt differs from TEXT"
    assert raw == TEXT.encode("utf-8"), "entry.txt not byte-identical to TEXT"
    assert not raw.endswith(b"\n"), "entry.txt has a trailing newline"
    validate(text)


if __name__ == "__main__":
    main()
