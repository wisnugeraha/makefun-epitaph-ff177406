#!/usr/bin/env python3.13
"""Famous Last Words: The Funniest Epitaph - entry program."""
import os

OUT = "/output/entry.txt"
STONE_LIMIT = 150


def carve() -> str:
    # one line of dying speech, nothing else: no stage directions, no footnote.
    return "I said I'd be back. I lied."


def chisel(line: str) -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(line)


def audit() -> tuple[int, int]:
    """read the stone back; confirm bytes vs the carver's cap."""
    with open(OUT, "rb") as fh:
        raw = fh.read()
    return len(raw), len(raw.decode("utf-8"))


def report() -> None:
    size, chars = audit()
    banner = "engraving sealed" if chars <= STONE_LIMIT else "OVER CAP"
    print(f"{banner}: {chars} chars / {size} bytes, cap {STONE_LIMIT}")
    print(f"stone reads: {open(OUT, encoding='utf-8').read()!r}")


if __name__ == "__main__":
    chisel(carve())
    report()
