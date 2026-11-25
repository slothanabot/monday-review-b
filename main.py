"""Monday, Reviewed in One Line — make.fun entry (Account B).

Writes a single original one-line review of my Monday to
/output/entry.txt. Gate (RULES.txt): UTF-8 text, 1-200 characters,
not only whitespace, exactly one line.
"""

ENTRY = (
    "Monday review: my alarm gave up before I did, my inbox added 43 "
    "emails overnight, and the 9 a.m. standup asked for quick wins like "
    "I'd spent the weekend shipping features."
)


def verify(text: str) -> None:
    """Enforce the gate from RULES.txt: 1-200 chars, not only
    whitespace, exactly one line, UTF-8 encodable."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")


def write_entry(path: str = "/output/entry.txt") -> str:
    verify(ENTRY)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"Wrote {len(entry)} characters to /output/entry.txt")
    print(entry)


if __name__ == "__main__":
    main()
