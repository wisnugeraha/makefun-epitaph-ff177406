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


if __name__ == "__main__":
    chisel(carve())
