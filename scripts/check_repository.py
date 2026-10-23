#!/usr/bin/env python3
"""Check the research/design submission using Python 3.10+ standard library.

This checks local materials, not a running application, stakeholder evidence,
OpenAPI semantics, external links, or supervisor approval. It does not contact
external services or change files. Review the Git staging area before publishing.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = frozenset({".git", ".local-audit", "__pycache__"})
REQUIRED_FILES = (
    "README.md",
    "docs/01-project-proposal.md",
    "docs/02-relevance-and-evidence.md",
    "docs/03-literature-review.md",
    "docs/04-existing-systems.md",
    "docs/05-technology-comparison.md",
    "docs/06-requirements.md",
    "docs/07-architecture.md",
    "docs/08-prototype.md",
    "docs/09-verification-plan.md",
    "docs/10-project-management.md",
    "docs/11-supervisor-feedback.md",
    "docs/12-submission.md",
    "docs/validation.md",
    "prototypes/openapi.yaml",
)
SOURCE_EXTENSIONS = (".mmd", ".drawio", ".puml", ".plantuml")
BINARY_EXTENSIONS = frozenset(
    {".exe", ".dll", ".so", ".dylib", ".a", ".o", ".obj", ".class", ".jar", ".pyc", ".zip"}
)
SECRET_EXTENSIONS = frozenset({".key", ".pem", ".p12", ".pfx", ".keystore"})
SECRET_NAMES = frozenset({"credentials.json", "token.json", "secrets.json", "secrets.yaml", "secrets.yml"})
EXECUTABLE_HEADERS = (b"MZ", b"\x7fELF", b"\xfe\xed\xfa\xce", b"\xfe\xed\xfa\xcf", b"\xcf\xfa\xed\xfe", b"\xce\xfa\xed\xfe")
SECRET_PATTERNS = (
    ("private key material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("provider credential-shaped literal", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b")),
    ("source hosting token-shaped literal", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{35,}\b")),
    ("cloud access key-shaped literal", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("bot token-shaped literal", re.compile(r"\b[0-9]{8,}:[A-Za-z0-9_-]{25,}\b")),
)
INLINE_LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return "outside repository"


def within_root(path: Path) -> bool:
    try:
        path.relative_to(ROOT)
        return True
    except ValueError:
        return False


def public_files() -> tuple[list[Path], list[str]]:
    """Prune private directories before descending; never follow symbolic links."""
    files: list[Path] = []
    errors: list[str] = []
    for directory, subdirectories, names in os.walk(ROOT, followlinks=False):
        base = Path(directory)
        allowed_subdirectories = []
        for name in subdirectories:
            if name in EXCLUDED_DIRECTORIES:
                continue
            child = base / name
            if child.is_symlink():
                errors.append(f"{display_path(child)}: symbolic directory is not allowed in this submission")
            else:
                allowed_subdirectories.append(name)
        subdirectories[:] = sorted(allowed_subdirectories)
        for name in sorted(names):
            path = base / name
            if path.is_symlink() or not within_root(path.resolve()):
                errors.append(f"{display_path(path)}: symbolic or escaping file is not allowed")
            else:
                files.append(path)
    return files, errors


def without_code_blocks(text: str) -> str:
    """Keep line positions while ignoring Markdown examples inside code fences."""
    lines = text.splitlines(keepends=True)
    fence_character = ""
    fence_size = 0
    for index, line in enumerate(lines):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match and not fence_character:
            fence_character = match.group(1)[0]
            fence_size = len(match.group(1))
            lines[index] = "\n" if line.endswith("\n") else ""
        elif fence_character:
            if match and match.group(1)[0] == fence_character and len(match.group(1)) >= fence_size:
                fence_character = ""
            lines[index] = "\n" if line.endswith("\n") else ""
    return "".join(lines)


def check_markdown_links(path: Path, text: str) -> list[str]:
    errors = []
    visible = without_code_blocks(text)
    for pattern in (INLINE_LINK, REFERENCE_LINK):
        for match in pattern.finditer(visible):
            raw_target = match.group(1).strip("<>")
            line = visible.count("\n", 0, match.start()) + 1
            location = f"{display_path(path)}:{line}"
            try:
                parsed = urlsplit(raw_target)
            except ValueError:
                errors.append(f"{location}: malformed link target")
                continue
            # External links and anchors alone are intentionally outside this check.
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            decoded = unquote(parsed.path)
            if "\x00" in decoded or "\\" in decoded:
                errors.append(f"{location}: local link contains an invalid path character")
                continue
            target = ((ROOT / decoded.lstrip("/")) if decoded.startswith("/") else (path.parent / decoded)).resolve()
            if not within_root(target):
                errors.append(f"{location}: local link escapes the repository")
            elif any(part in EXCLUDED_DIRECTORIES for part in target.relative_to(ROOT).parts):
                errors.append(f"{location}: local link points to excluded private material")
            elif not target.exists():
                errors.append(f"{location}: missing local link target {display_path(target)}")
    return errors


def main() -> int:
    files, errors = public_files()
    file_set = set(files)
    markdown_count = 0
    svg_count = 0

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if path not in file_set:
            errors.append(f"{relative}: required material is missing")
        elif not path.stat().st_size:
            errors.append(f"{relative}: required material is empty")

    for path in files:
        name = path.name.lower()
        extension = path.suffix.lower()
        relative = display_path(path)
        if extension == ".go" or name in {"go.mod", "go.sum", "go.work", "go.work.sum"}:
            errors.append(f"{relative}: application implementation is outside this research/design baseline")
        if extension in BINARY_EXTENSIONS:
            errors.append(f"{relative}: executable, build artifact, or archive is not allowed")
        if name == ".env" or name.startswith(".env.") or name in SECRET_NAMES or extension in SECRET_EXTENSIONS:
            errors.append(f"{relative}: credential or environment file is not allowed")

        try:
            data = path.read_bytes()
        except OSError:
            errors.append(f"{relative}: file cannot be read")
            continue
        if data.startswith(EXECUTABLE_HEADERS):
            errors.append(f"{relative}: executable file signature detected")
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError:
            errors.append(f"{relative}: expected a UTF-8 text material at this stage")
            continue

        for description, pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{relative}:{line}: {description}; value withheld")

        if extension == ".md":
            markdown_count += 1
            errors.extend(check_markdown_links(path, text))
        elif extension == ".svg":
            svg_count += 1
            try:
                element = ET.fromstring(data)
                if element.tag not in {"svg", "{http://www.w3.org/2000/svg}svg"}:
                    errors.append(f"{relative}: XML root is not an SVG element")
            except ET.ParseError as error:
                row, column = error.position
                errors.append(f"{relative}:{row}:{column}: malformed SVG XML")
            if not any(path.with_suffix(suffix) in file_set for suffix in SOURCE_EXTENSIONS):
                errors.append(f"{relative}: matching editable diagram source is missing")

    diagrams = [path for path in files if path.suffix.lower() == ".svg" and path.parent == ROOT / "diagrams"]
    if len(diagrams) < 3:
        errors.append("diagrams/: at least three SVG diagrams with matching editable sources are required")

    if errors:
        print(f"FAIL: {len(errors)} repository material issue(s)")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    print(f"PASS: {len(REQUIRED_FILES)} required files; {markdown_count} Markdown files and local links; {svg_count} SVG files and editable sources.")
    print(f"Checked {len(files)} public text files for excluded implementation/build material and common credential patterns.")
    print("Not checked: external links, Markdown anchors, OpenAPI semantics, runtime behavior, empirical claims, or approvals.")
    return 0


if __name__ == "__main__":
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10 or newer is required.")
    raise SystemExit(main())
