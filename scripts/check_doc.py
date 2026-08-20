#!/usr/bin/env python3
"""Lint a markdown document for Google Developer Documentation Style violations.

Usage:
    check_doc.py <file.md>

Flags first-person pronouns, passive constructions, marketing fluff,
future-tense "will", non-sentence-case headings, and trailing "if/to" clauses.
Skips fenced code blocks and inline code spans. Exit code 0 = no violations;
1 = violations found.
"""
import re
import sys
from pathlib import Path

# Common -ed words that are adjectives, not passive participles (e.g. "is malformed").
ADJECTIVE_ED = {
    "malformed", "related", "dedicated", "automated", "distributed", "embedded",
    "intended", "included", "expected", "located", "deployed", "designed",
    "structured", "documented", "billed", "increased", "decreased", "unmanaged",
}
FIRST_PERSON = re.compile(r"\b(we|our|ours|us|let's|i)\b", re.IGNORECASE)
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(\w+ed)\b", re.IGNORECASE)
FLUFF = re.compile(r"\b(seamless(ly)?|effortless(ly)?|powerful|robust|cutting-edge|best-in-class|revolutionary|simply|just (?:want|need))\b", re.IGNORECASE)
FUTURE = re.compile(r"\bwill (?:return|send|receive|create|be|provide|generate|display|show|occur|happen|start|stop|update)\b", re.IGNORECASE)
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
INLINE_CODE = re.compile(r"`[^`]*`")
# Trailing condition: the final clause (after the last comma/semicolon/colon)
# begins with "if" or "when", putting the condition after the action.
TRAILING_COND = re.compile(r"^(if|when)\b", re.IGNORECASE)


def strip_code(text: str) -> str:
    """Remove inline code spans and their contents."""
    return INLINE_CODE.sub(" ", text)


def lint(path: Path) -> list:
    problems = []
    in_fence = False
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue

        text = strip_code(stripped)
        for name, rx in (("first-person", FIRST_PERSON), ("passive", PASSIVE),
                         ("fluff", FLUFF), ("future-tense", FUTURE)):
            m = rx.search(text)
            if not m:
                continue
            if name == "passive" and m.group(1).lower() in ADJECTIVE_ED:
                continue
            problems.append(f"{lineno}: {name}: '{m.group(0)}' -> {stripped}")

        hm = HEADING.match(stripped)
        if hm:
            words = hm.group(2).split()
            if len(words) > 1:
                # sentence case: only the first word is capitalized. Flag when three or
                # more non-first words are capitalized (excludes all-caps acronyms and
                # short connectives like "to"/"on"/"with"), which indicates Title Case.
                bad = [w for w in words[1:]
                       if w[0].isupper()
                       and not re.match(r"^[A-Z0-9&./-]+$", w)
                       and not re.match(r"^[A-Za-z]{1,2}$", w)]
                if len(bad) >= 3:
                    problems.append(f"{lineno}: heading not sentence case: '{bad[0]}' in -> {stripped}")

        # Only check the final clause for a trailing condition.
        tail = re.split(r"[;,]", text)[-1].strip()
        if TRAILING_COND.match(tail):
            problems.append(f"{lineno}: condition at end of sentence -> {stripped}")
    return problems


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: check_doc.py <file.md>", file=sys.stderr)
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(2)
    problems = lint(path)
    if problems:
        for p in problems:
            print(p)
        print(f"\n{len(problems)} violation(s) found.")
        sys.exit(1)
    print("No violations found.")
    sys.exit(0)


if __name__ == "__main__":
    main()
