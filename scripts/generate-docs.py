#!/usr/bin/env python3
"""Generate catalog, README tables, and logic-doc index from solution headers."""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGUAGES_DIR = ROOT / "languages"
DOCS_DIR = ROOT / "docs"
GUIDE_DIR = DOCS_DIR / "guide"
CATALOG_DIR = DOCS_DIR / "catalog"
LOGIC_DOCS_DIR = DOCS_DIR / "logic"
GENERATED_BEGIN = "<!-- BEGIN GENERATED -->"
GENERATED_END = "<!-- END GENERATED -->"

LANGUAGE_META: dict[str, dict[str, str]] = {
    "c": {"display": "C", "anchor": "c"},
    "cpp": {"display": "C++", "anchor": "cpp"},
    "csharp": {"display": "C#", "anchor": "csharp"},
    "dart": {"display": "Dart", "anchor": "dart"},
    "go": {"display": "Go", "anchor": "go"},
    "groovy": {"display": "Groovy", "anchor": "groovy"},
    "java": {"display": "Java", "anchor": "java"},
    "javascript": {"display": "JavaScript", "anchor": "javascript"},
    "kotlin": {"display": "Kotlin", "anchor": "kotlin"},
    "lua": {"display": "Lua", "anchor": "lua"},
    "php": {"display": "PHP", "anchor": "php"},
    "python": {"display": "Python", "anchor": "python"},
    "ruby": {"display": "Ruby", "anchor": "ruby"},
    "rust": {"display": "Rust", "anchor": "rust"},
    "scala": {"display": "Scala", "anchor": "scala"},
    "shell": {"display": "Shell", "anchor": "shell"},
    "sql": {"display": "SQL", "anchor": "sql"},
    "typescript": {"display": "TypeScript", "anchor": "typescript"},
}

SOLUTION_EXTENSIONS = {
    ".c",
    ".cpp",
    ".cs",
    ".dart",
    ".go",
    ".groovy",
    ".java",
    ".js",
    ".kt",
    ".lua",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".scala",
    ".sh",
    ".sql",
    ".ts",
}


@dataclass
class Solution:
    slug: str
    title: str
    link: str
    kyu: int
    language: str
    rel_path: str

    @property
    def kyu_label(self) -> str:
        return f"{self.kyu} kyu"


@dataclass
class LogicDoc:
    slug: str
    title: str
    kyu: int
    rel_path: str


def strip_comment_prefix(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith("///"):
        return stripped[3:].strip()
    if stripped.startswith("//"):
        return stripped[2:].strip()
    if stripped.startswith("--"):
        return stripped[2:].strip()
    if stripped.startswith("#"):
        return stripped[1:].strip()
    if stripped.startswith("*"):
        return stripped.lstrip("*").strip()
    return stripped


def extract_header_block(content: str) -> str:
    text = content.lstrip()
    if text.startswith('"""'):
        match = re.search(r'"""(.*?)"""', text, re.DOTALL)
        return match.group(1).strip() if match else ""

    lines: list[str] = []
    for line in content.splitlines()[:30]:
        stripped = line.strip()
        if not stripped:
            if lines:
                lines.append("")
            continue

        if stripped.startswith("/*"):
            lines.append(strip_comment_prefix(stripped.lstrip("/")))
            continue
        if stripped.startswith(("//", "--", "#", "*", "///")):
            lines.append(strip_comment_prefix(stripped))
            continue
        if stripped.endswith("*/"):
            lines.append(strip_comment_prefix(stripped.rstrip("*/")))
            break
        if lines:
            break
        if re.match(
            r"^(package|import|export|def |function |public |class |fn |module )",
            stripped,
        ):
            break

    return "\n".join(lines).strip()


def parse_header(content: str) -> dict[str, str]:
    block = extract_header_block(content)
    title = re.search(r"^Title:\s*(.+)$", block, re.MULTILINE | re.IGNORECASE)
    link = re.search(r"^Link:\s*(\S+)$", block, re.MULTILINE | re.IGNORECASE)
    difficulty = re.search(
        r"^Difficulty:\s*(.+)$", block, re.MULTILINE | re.IGNORECASE
    )
    return {
        "title": title.group(1).strip() if title else "",
        "link": link.group(1).strip() if link else "",
        "difficulty": difficulty.group(1).strip() if difficulty else "",
    }


def parse_kyu(folder_name: str) -> int:
    match = re.fullmatch(r"(\d)kyu", folder_name)
    if not match:
        raise ValueError(f"Unexpected kyu folder: {folder_name}")
    return int(match.group(1))


def logic_doc_rel_path(slug: str, kyu: int) -> str | None:
    path = LOGIC_DOCS_DIR / f"{kyu}kyu" / f"{slug}.md"
    if not path.is_file():
        return None
    return path.relative_to(ROOT).as_posix()


def discover_solutions() -> list[Solution]:
    solutions: list[Solution] = []
    for lang_dir in sorted(LANGUAGES_DIR.iterdir()):
        if not lang_dir.is_dir():
            continue
        language = lang_dir.name
        if language not in LANGUAGE_META:
            continue

        for path in sorted(lang_dir.rglob("*")):
            if not path.is_file() or path.suffix not in SOLUTION_EXTENSIONS:
                continue
            kyu = parse_kyu(path.parent.name)
            header = parse_header(path.read_text(encoding="utf-8"))
            rel_path = path.relative_to(ROOT).as_posix()
            solutions.append(
                Solution(
                    slug=path.stem,
                    title=header["title"] or path.stem.replace("-", " ").title(),
                    link=header["link"],
                    kyu=kyu,
                    language=language,
                    rel_path=rel_path,
                )
            )
    return solutions


def discover_logic_docs() -> list[LogicDoc]:
    docs: list[LogicDoc] = []
    if not LOGIC_DOCS_DIR.is_dir():
        return docs

    for path in sorted(LOGIC_DOCS_DIR.rglob("*.md")):
        if path.name == "README.md":
            continue
        kyu = parse_kyu(path.parent.name)
        content = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
        docs.append(
            LogicDoc(
                slug=path.stem,
                title=title,
                kyu=kyu,
                rel_path=path.relative_to(LOGIC_DOCS_DIR).as_posix(),
            )
        )
    return docs


def kyu_sort_key(kyu: int) -> int:
    return -kyu


def language_sort_key(language: str) -> str:
    return LANGUAGE_META[language]["display"].lower()


def rel_from(base_dir: Path, target: Path) -> str:
    return os.path.relpath(target, base_dir).replace("\\", "/")


def format_language_links(solutions: list[Solution], base_dir: Path) -> str:
    ordered = sorted(solutions, key=lambda s: language_sort_key(s.language))
    parts = []
    for sol in ordered:
        display = LANGUAGE_META[sol.language]["display"]
        target = ROOT / sol.rel_path
        parts.append(f"[{display}]({rel_from(base_dir, target)})")
    return " — ".join(parts)


def format_logic_link(slug: str, kyu: int, base_dir: Path) -> str:
    path = LOGIC_DOCS_DIR / f"{kyu}kyu" / f"{slug}.md"
    if not path.is_file():
        return "—"
    return f"[logic]({rel_from(base_dir, path)})"


def build_kyu_sections(
    grouped: dict[int, list[Solution]],
    *,
    by_language: str | None = None,
    link_base_dir: Path | None = None,
) -> str:
    sections: list[str] = []
    for kyu in sorted(grouped.keys(), key=kyu_sort_key):
        entries = grouped[kyu]
        if by_language:
            entries = [s for s in entries if s.language == by_language]
            if not entries:
                continue
            entries = sorted(entries, key=lambda s: s.title.lower())
            rows = [
                f"| {sol.title} | [{Path(sol.rel_path).name}]({(ROOT / sol.rel_path).relative_to(LANGUAGES_DIR / by_language).as_posix()}) |"
                for sol in entries
            ]
            table = "| Exercise | File |\n|----------|------|\n" + "\n".join(rows)
        else:
            by_slug: dict[str, list[Solution]] = defaultdict(list)
            for sol in entries:
                by_slug[sol.slug].append(sol)

            rows = []
            for slug in sorted(by_slug.keys(), key=lambda s: by_slug[s][0].title.lower()):
                group = by_slug[slug]
                title = group[0].title
                base_dir = link_base_dir or CATALOG_DIR
                logic = format_logic_link(slug, kyu, base_dir)
                solutions_cell = format_language_links(group, base_dir)
                rows.append(f"| {title} | {logic} | {solutions_cell} |")
            table = (
                "| Exercise | Logic | Solutions |\n"
                "|----------|-------|----------|\n" + "\n".join(rows)
            )

        sections.append(f"### {kyu} kyu\n\n{table}")
    return "\n\n".join(sections)


def render_language_readme(language: str, solutions: list[Solution]) -> str:
    meta = LANGUAGE_META[language]
    display = meta["display"]
    anchor = meta["anchor"]
    lang_solutions = [s for s in solutions if s.language == language]
    grouped: dict[int, list[Solution]] = defaultdict(list)
    for sol in lang_solutions:
        grouped[sol.kyu].append(sol)

    generated = build_kyu_sections(grouped, by_language=language)
    if not generated:
        generated = "_No solutions yet._"

    return f"""# {display}

Personal [Codewars](https://www.codewars.com/) solutions in {display}.

- **Run locally:** [running.md#{anchor}](../../docs/guide/running.md#{anchor})
- **Conventions:** [conventions.md](../../docs/guide/conventions.md)
- **Catalog:** [catalog](../../docs/catalog/README.md)
- **Logic:** [logic](../../docs/logic/README.md)

## Solutions

Kyu levels run from **8 kyu** (easiest) to **1 kyu** (hardest). See [conventions](../../docs/guide/conventions.md) for layout details.

{GENERATED_BEGIN}
{generated}
{GENERATED_END}

## License

These {display} files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../../README.md#license) in the repository root.
"""


def render_catalog_readme(solutions: list[Solution]) -> str:
    grouped: dict[int, list[Solution]] = defaultdict(list)
    for sol in solutions:
        grouped[sol.kyu].append(sol)

    generated = build_kyu_sections(grouped)
    unique_katas = len({(s.slug, s.kyu) for s in solutions})
    languages = len({s.language for s in solutions})

    return f"""# Solution catalog

Every kata in this repository, grouped by difficulty. Each row links to the logic doc and all implemented solutions.

| Katas | Solutions | Languages |
|------:|----------:|----------:|
| {unique_katas} | {len(solutions)} | {languages} |

[Logic](../logic/README.md) · [Conventions](../guide/conventions.md) · [Docs](../README.md)

_Regenerate with `python3 scripts/generate-docs.py`._

{GENERATED_BEGIN}
{generated}
{GENERATED_END}
"""


def render_logic_docs_readme(logic_docs: list[LogicDoc]) -> str:
    grouped: dict[int, list[LogicDoc]] = defaultdict(list)
    for doc in logic_docs:
        grouped[doc.kyu].append(doc)

    sections: list[str] = []
    for kyu in sorted(grouped.keys(), key=kyu_sort_key):
        rows = []
        for doc in sorted(grouped[kyu], key=lambda item: item.title.lower()):
            rows.append(f"| {doc.title} | [{doc.slug}.md]({doc.rel_path}) |")
        table = "| Kata | Logic |\n|------|-------|\n" + "\n".join(rows)
        sections.append(f"## {kyu} kyu\n\n{table}")

    generated = "\n\n".join(sections) if sections else "_No logic docs yet._"

    return f"""# Logic

Behavioral contracts and pseudocode — `docs/logic/<N>kyu/<slug>.md`.

Content is hand-authored; only the index below is generated.

[Catalog](../catalog/README.md) · [Conventions](../guide/conventions.md) · [Docs](../README.md)

{GENERATED_BEGIN}
{generated}
{GENERATED_END}
"""


def render_docs_readme(solutions: list[Solution], logic_docs: list[LogicDoc]) -> str:
    unique_katas = len({(s.slug, s.kyu) for s in solutions})
    languages = len({s.language for s in solutions})

    return f"""# Documentation

Three layers under `docs/`:

| Layer | Path | Role |
|-------|------|------|
| **Guide** | [guide/](guide/) | How to work with the repo (hand-authored) |
| **Catalog** | [catalog/](catalog/) | Solution index from code (generated) |
| **Logic** | [logic/](logic/) | Kata specs and pseudocode (hand-authored + generated index) |

## Quick links

| | |
|---|---|
| [Solution catalog](catalog/README.md) | {unique_katas} katas · {len(solutions)} solutions · {languages} languages |
| [Logic index](logic/README.md) | {len(logic_docs)} behavioral contracts |
| [Conventions](guide/conventions.md) | Layout, headers, workflow |
| [Running locally](guide/running.md) | Per-language run commands |

## Layout

```
docs/
├── README.md           # this file
├── guide/              # reference (hand-authored)
│   ├── conventions.md
│   └── running.md
├── catalog/            # generated — solution index + katas.json
│   ├── README.md
│   └── katas.json
└── logic/              # kata specs (hand-authored) + generated index
    ├── README.md
    └── <N>kyu/<slug>.md
```

Regenerate catalog and indexes: `python3 scripts/generate-docs.py`
"""


def render_root_readme(solutions: list[Solution]) -> str:
    unique_katas = len({(s.slug, s.kyu) for s in solutions})
    languages = sorted(LANGUAGE_META.keys(), key=language_sort_key)

    lang_rows = []
    for language in languages:
        display = LANGUAGE_META[language]["display"]
        count = sum(1 for s in solutions if s.language == language)
        if count == 0:
            continue
        lang_rows.append(
            f"| {display} | {count} | [languages/{language}](languages/{language}/README.md) |"
        )

    stats_block = (
        f"- **Unique katas:** {unique_katas}\n"
        f"- **Total solutions:** {len(solutions)}\n"
        f"- **Languages:** {len({s.language for s in solutions})}"
    )

    return f"""# Codewars Challenges

A collection of my solutions to [Codewars](https://www.codewars.com/) challenges, organized by language and difficulty.

## Quick links

- [Documentation](docs/README.md)
- [Solution catalog](docs/catalog/README.md)
- [Logic specs](docs/logic/README.md)
- [Running locally](docs/guide/running.md)

## Stats

{GENERATED_BEGIN}
{stats_block}
{GENERATED_END}

_Regenerate with `python3 scripts/generate-docs.py`._

## Languages

| Language | Solutions | README |
|----------|-----------|--------|
{chr(10).join(lang_rows)}

## Repository layout

```
dsa-codewars/
├── docs/
│   ├── guide/            # conventions + running (hand-authored)
│   ├── catalog/          # solution index (generated)
│   └── logic/            # kata specs + index
├── languages/
│   ├── python/
│   │   ├── README.md     # solution table (generated)
│   │   └── 8kyu/
│   └── ...
└── scripts/
    └── generate-docs.py
```

Within each language directory, files live in kyu subfolders (`8kyu/` … `1kyu/`). **A higher kyu number means an easier exercise; a lower kyu means a harder one.**

## License

This repository is **personal practice only**: my own solutions to [Codewars](https://www.codewars.com/) katas, kept for learning and reference. It is **not** affiliated with or endorsed by Codewars.

Exercise descriptions, tests, and trademarks belong to Codewars and the respective kata authors. Code in this repo is shared as-is, without warranty. If you use or adapt anything here, you remain responsible for complying with Codewars' terms and with any license that applies to the original kata content.
"""


def write_catalog_json(solutions: list[Solution]) -> None:
    by_kata: dict[str, dict] = {}
    for sol in solutions:
        key = f"{sol.kyu}:{sol.slug}"
        if key not in by_kata:
            logic_doc = logic_doc_rel_path(sol.slug, sol.kyu)
            by_kata[key] = {
                "slug": sol.slug,
                "title": sol.title,
                "kyu": sol.kyu,
                "link": sol.link,
                "logic_doc": logic_doc,
                "solutions": [],
            }
        by_kata[key]["solutions"].append(
            {"language": sol.language, "path": sol.rel_path}
        )

    catalog = sorted(
        by_kata.values(),
        key=lambda item: (-item["kyu"], item["title"].lower()),
    )
    for item in catalog:
        item["solutions"] = sorted(
            item["solutions"], key=lambda s: language_sort_key(s["language"])
        )

    CATALOG_DIR.mkdir(exist_ok=True)
    (CATALOG_DIR / "katas.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    solutions = discover_solutions()
    if not solutions:
        raise SystemExit("No solutions found under languages/")

    logic_docs = discover_logic_docs()

    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    (CATALOG_DIR / "README.md").write_text(
        render_catalog_readme(solutions), encoding="utf-8"
    )
    write_catalog_json(solutions)
    (DOCS_DIR / "README.md").write_text(
        render_docs_readme(solutions, logic_docs), encoding="utf-8"
    )
    (ROOT / "README.md").write_text(render_root_readme(solutions), encoding="utf-8")

    LOGIC_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    (LOGIC_DOCS_DIR / "README.md").write_text(
        render_logic_docs_readme(logic_docs), encoding="utf-8"
    )

    for language in sorted(LANGUAGE_META.keys(), key=language_sort_key):
        lang_dir = LANGUAGES_DIR / language
        if not lang_dir.is_dir():
            continue
        (lang_dir / "README.md").write_text(
            render_language_readme(language, solutions), encoding="utf-8"
        )

    active_languages = len({s.language for s in solutions})
    print(
        f"Generated docs for {len(solutions)} solutions across {active_languages} languages "
        f"and {len(logic_docs)} logic docs."
    )


if __name__ == "__main__":
    main()
