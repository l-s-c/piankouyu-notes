"""Refresh the installed skill's offline copy of the archive's Markdown notes."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import quote, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "skills/piankouyu/references"
GITHUB = "https://github.com/l-s-c/piankouyu-notes/blob/main/"
ROOT_DOCS = (
    "clips.md", "dialogues.md", "posts.md", "recordings.md",
    "sources.md", "voice.md", "xiaohongshu.md",
)
LINK_TARGET = re.compile(r"(?<=\]\()([^\s)]+)(?=\))")


def render(source, sources):
    def local_link(match):
        url = urlsplit(match[0])
        if url.scheme or url.netloc or not url.path:
            return match[0]
        target = (source.parent / unquote(url.path)).resolve()
        if target in sources:
            return match[0]
        if not target.is_file():
            raise ValueError(f"Broken link in {source.relative_to(ROOT)}: {match[0]}")
        public_path = quote(target.relative_to(ROOT).as_posix())
        return GITHUB + url._replace(path=public_path).geturl()

    return LINK_TARGET.sub(local_link, source.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report differences without writing")
    check = parser.parse_args().check
    sources = {ROOT / name for name in ROOT_DOCS}
    for folder in ("knowledge", "sessions"):
        sources.update((ROOT / folder).glob("*.md"))
    problems = []
    for source in sorted(sources):
        destination = DEST / source.relative_to(ROOT)
        expected = render(source, sources).encode("utf-8")
        if destination.is_file() and destination.read_bytes() == expected:
            continue
        if check:
            problems.append(f"Out of sync: {destination.relative_to(ROOT)}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(expected)

    # Archive files may have been renamed. Report the old copies for manual review.
    managed = {source.relative_to(ROOT) for source in sources}
    for destination in sorted(DEST.rglob("*.md")):
        if destination.relative_to(DEST) not in managed:
            problems.append(f"Unexpected reference: {destination.relative_to(ROOT)}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"{len(sources)} offline reference files in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
