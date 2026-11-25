"""One Line, One Laugh — a make.fun micro entry.

The whole entry is a single funny line, defined once as a constant
and printed / written out. No setup, no explanation — the line is the joke.
"""

# The joke: the password itself is the word "incorrect", so the system's
# own error message ("your password is incorrect") becomes a true statement
# every time the user forgets it — the computer is helpfully correct.
LINE = "My password expired, so I changed it to 'incorrect' — now every time I forget it, the computer helpfully reminds me: your password is incorrect."


def validate_line(line: str, max_chars: int = 200) -> str:
    """Check the entry line: non-empty, single line, within the limit."""
    assert line, "entry line must not be empty"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= max_chars, f"line is {len(line)} chars, over the {max_chars}-char limit"
    assert line == line.strip(), "entry line must not have leading/trailing whitespace"
    return line


LINE = validate_line(LINE)


OUTPUT_DIR = "/output"
OUTPUT_PATH = f"{OUTPUT_DIR}/entry.txt"


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to the output file, creating the directory.

    Returns the path written to, so callers can confirm where it landed.
    The file is written with no trailing newline: the gate counts the
    entry's characters exactly, so the file holds the line and nothing else.
    """
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main() -> None:
    """Print the entry line and write it to the output file."""
    print(LINE)
    write_entry()


if __name__ == "__main__":
    main()
