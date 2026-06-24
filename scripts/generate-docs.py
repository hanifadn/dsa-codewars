#!/usr/bin/env python3
"""Generate catalog and README tables from solution file headers."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGUAGES_DIR = ROOT / "languages"
CATALOG_DIR = ROOT / "catalog"
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
    "lua": {"display": "Lua", "anchor": "lua"},
    "python": {"display": "Python", "anchor": "python"},
    "ruby": {"display": "Ruby", "anchor": "ruby"},
    "rust": {"display": "Rust", "anchor": "rust"},
    "scala": {"display": "Scala", "anchor": "scala"},
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
    ".lua",
    ".py",
    ".rb",
    ".rs",
    ".scala",
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


def kyu_sort_key(kyu: int) -> int:
    return -kyu


def language_sort_key(language: str) -> str:
    return LANGUAGE_META[language]["display"].lower()


def format_language_links(solutions: list[Solution]) -> str:
    ordered = sorted(solutions, key=lambda s: language_sort_key(s.language))
    parts = []
    for sol in ordered:
        display = LANGUAGE_META[sol.language]["display"]
        parts.append(f"[{display}](../{sol.rel_path})")
    return " — ".join(parts)


def build_kyu_sections(
    grouped: dict[int, list[Solution]],
    *,
    by_language: str | None = None,
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
                rows.append(f"| {title} | {format_language_links(group)} |")
            table = "| Exercise | Solutions |\n|----------|----------|\n" + "\n".join(rows)

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

- **Run locally:** [docs/RUNNING.md#{anchor}](../../docs/RUNNING.md#{anchor})
- **Conventions:** [docs/CONVENTIONS.md](../../docs/CONVENTIONS.md)
- **Browse by kata:** [catalog](../../catalog/README.md)

## Solutions

Kyu levels run from **8 kyu** (easiest) to **1 kyu** (hardest). See [Conventions](../../docs/CONVENTIONS.md) for layout details.

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

    return f"""# Kata catalog

Browse every kata implemented in this repository, grouped by difficulty.

- **Unique katas:** {unique_katas}
- **Total solutions:** {len(solutions)}
- **Languages:** {languages}

See [Conventions](../docs/CONVENTIONS.md) for how solutions are organized. Regenerate this file with `python3 scripts/generate-docs.py`.

{GENERATED_BEGIN}
{generated}
{GENERATED_END}
"""


def render_root_readme(solutions: list[Solution]) -> str:
    unique_katas = len({(s.slug, s.kyu) for s in solutions})
    languages = sorted(LANGUAGE_META.keys(), key=language_sort_key)

    lang_rows = []
    for language in languages:
        display = LANGUAGE_META[language]["display"]
        count = sum(1 for s in solutions if s.language == language)
        lang_rows.append(
            f"| {display} | {count} | [languages/{language}](languages/{language}/README.md) |"
        )

    stats_block = (
        f"- **Unique katas:** {unique_katas}\n"
        f"- **Total solutions:** {len(solutions)}\n"
        f"- **Languages:** {len(languages)}"
    )

    return f"""# Codewars Challenges

A collection of my solutions to [Codewars](https://www.codewars.com/) challenges, organized by language and difficulty.

## Quick links

- [Browse by kata](catalog/README.md)
- [Conventions](docs/CONVENTIONS.md)
- [Running locally](docs/RUNNING.md)

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
├── catalog/          # kata-centric index (generated)
├── docs/             # conventions and run instructions
├── languages/
│   ├── python/
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
            by_kata[key] = {
                "slug": sol.slug,
                "title": sol.title,
                "kyu": sol.kyu,
                "link": sol.link,
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

    CATALOG_DIR.mkdir(exist_ok=True)
    (CATALOG_DIR / "README.md").write_text(
        render_catalog_readme(solutions), encoding="utf-8"
    )
    write_catalog_json(solutions)
    (ROOT / "README.md").write_text(render_root_readme(solutions), encoding="utf-8")

    for language in sorted(LANGUAGE_META.keys(), key=language_sort_key):
        lang_dir = LANGUAGES_DIR / language
        if not lang_dir.is_dir():
            continue
        (lang_dir / "README.md").write_text(
            render_language_readme(language, solutions), encoding="utf-8"
        )

    print(f"Generated docs for {len(solutions)} solutions across {len(LANGUAGE_META)} languages.")


if __name__ == "__main__":
    main()
