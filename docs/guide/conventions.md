# Conventions

How this repository is organized and how to add solutions.

[← Documentation](../README.md)

## Architecture

```
dsa-codewars/
├── docs/
│   ├── guide/          # this file + running.md (hand-authored)
│   ├── catalog/        # solution index (generated)
│   └── logic/          # kata specs (hand-authored)
├── languages/
│   └── <lang>/<N>kyu/<slug>.<ext>
└── scripts/
    └── generate-docs.py
```

| Layer | Maintained by | Purpose |
|-------|---------------|---------|
| `docs/logic/` | Problem solver | Pseudocode and behavioral contract per kata |
| `languages/` | Coder | Implementations |
| `docs/catalog/` | `generate-docs.py` | Index of what exists |

Kyu folders run **8 → 1** (higher kyu = easier).

## Solution files

**One file per kata per language.** Filename = kata slug in kebab-case (`array-plus-array.py`).

### Header (required)

| Field | Example |
|-------|---------|
| Title | `Array plus array` |
| Link | `https://www.codewars.com/kata/5a2be17aee1aaefe2a000151` |
| Difficulty | `8 kyu` |
| Description | Optional problem statement |

Use the comment style natural to the language.

### Language notes

| Language | Note |
|----------|------|
| Java / C# | Public type may follow Codewars skeleton; filename uses slug |
| Go | `package kata`, no `main` |
| Shell | Input via `$1`, output via stdout |
| SQL | `SELECT` against Codewars SQLite schema |
| C, C++, Rust, Java | No entry point in snippet — see [running.md](running.md) |

## Workflow

1. Write or verify logic spec at `docs/logic/<N>kyu/<slug>.md`.
2. Add `languages/<language>/<N>kyu/<slug>.<ext>` with header.
3. Run `python3 scripts/generate-docs.py`.

## Generated artifacts

Do not hand-edit content between `<!-- BEGIN GENERATED -->` and `<!-- END GENERATED -->`.

| Path | Generator |
|------|-----------|
| `docs/catalog/README.md`, `katas.json` | `generate-docs.py` |
| `docs/logic/README.md` | `generate-docs.py` |
| `docs/README.md` | `generate-docs.py` |
| `languages/*/README.md` | `generate-docs.py` |
| Root `README.md` stats | `generate-docs.py` |
