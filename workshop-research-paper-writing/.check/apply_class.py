#!/usr/bin/env python3
"""Apply a Marp local class directive to specific slides.

Usage: apply_class.py <file.md> <classname> <slide numbers...>
Merges with an existing `<!-- _class: ... -->` directive if present.
"""
import re
import sys


def split_deck(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        front = "\n".join(lines[: end + 1])
        rest = lines[end + 1 :]
    else:
        front, rest = None, lines
    slides, cur = [], []
    for ln in rest:
        if ln.strip() == "---" and ln == "---":
            slides.append("\n".join(cur))
            cur = []
        else:
            cur.append(ln)
    slides.append("\n".join(cur))
    return front, slides


def join_deck(front, slides):
    body = "\n---\n".join(slides)
    return (front + "\n" + body) if front is not None else body


def add_class(slide, cls):
    m = re.search(r"^<!--\s*_class:\s*(.+?)\s*-->\s*$", slide, re.M)
    if m:
        existing = m.group(1).split()
        if cls in existing:
            return slide
        return slide[: m.start(1)] + " ".join(existing + [cls]) + slide[m.end(1) :]
    stripped = slide.lstrip("\n")
    lead = slide[: len(slide) - len(stripped)] or "\n"
    return lead + "<!-- _class: %s -->\n" % cls + stripped


def main():
    path, cls = sys.argv[1], sys.argv[2]
    nums = {int(n) for n in sys.argv[3:]}
    front, slides = split_deck(open(path).read())
    for n in sorted(nums):
        if 1 <= n <= len(slides):
            slides[n - 1] = add_class(slides[n - 1], cls)
        else:
            print("  ! slide %d out of range (deck has %d)" % (n, len(slides)))
    open(path, "w").write(join_deck(front, slides))
    print("  applied '%s' to %d slide(s) in %s" % (cls, len(nums), path))


if __name__ == "__main__":
    main()
