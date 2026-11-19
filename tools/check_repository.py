"""Check portable documentation and skill metadata using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)")


def inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def check_markdown(path: Path, root: Path, skill: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    label = path.relative_to(root).as_posix()
    if "\ufffd" in text:
        errors.append(f"{label}: replacement character found")
    if "file:" in text.lower() or re.search(r"\b[A-Za-z]:[\\/]", text):
        errors.append(f"{label}: machine-local path or file URI found")
    if text.count("```") % 2:
        errors.append(f"{label}: unclosed code fence")
    for match in LINK.finditer(text):
        target = unquote(match.group(1) or match.group(2))
        url = urlsplit(target)
        if url.scheme in {"https", "http"}:
            continue
        if url.scheme or target.startswith(("/", "\\")):
            errors.append(f"{label}: nonportable link {target}")
            continue
        destination = (path.parent / url.path).resolve() if url.path else path
        if not inside(destination, root):
            errors.append(f"{label}: link escapes repository: {target}")
        elif not destination.exists():
            errors.append(f"{label}: missing link target: {target}")
        elif inside(path, skill) and not inside(destination, skill):
            errors.append(f"{label}: installed skill depends on repository-only file: {target}")
        if url.fragment:
            errors.append(f"{label}: anchor links need explicit review: {target}")
    return errors


def check_skill(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        return ["SKILL.md: missing plain UTF-8 YAML frontmatter"]
    fields = dict(re.findall(r"^(name|description): (.+)$", match.group(1), re.M))
    errors = []
    if fields.get("name") != "gmp-sil-workbench":
        errors.append("SKILL.md: unexpected skill name")
    description = fields.get("description", "")
    if not description or len(description) > 1024:
        errors.append("SKILL.md: description must contain 1 to 1024 characters")
    if re.search(r"\[TODO:.*\]", text):
        errors.append("SKILL.md: unfinished placeholder")
    return errors


def scan(root: Path) -> list[str]:
    root = root.resolve()
    skill = root / "skills" / "gmp-sil-workbench"
    entry = skill / "SKILL.md"
    if not entry.is_file():
        return ["Missing skills/gmp-sil-workbench/SKILL.md"]
    errors = check_skill(entry)
    for path in sorted(root.rglob("*.md")):
        if ".git" not in path.relative_to(root).parts:
            errors.extend(check_markdown(path.resolve(), root, skill))
    return errors


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[1]
    findings = scan(repository)
    for finding in findings:
        print(finding)
    if not findings:
        print("Repository links, portability, and skill metadata: passed")
    sys.exit(bool(findings))
