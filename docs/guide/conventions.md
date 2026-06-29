# Conventions

This repository stores personal [Codewars](https://www.codewars.com/) solutions organized by language and difficulty.

## Repository layout

```
dsa-codewars/
├── catalog/              # kata-centric index (generated)
├── docs/                 # shared documentation
├── languages/
│   ├── python/
│   │   ├── README.md     # solution table (generated)
│   │   └── 8kyu/
│   │       └── kata-slug.py
│   └── ...
└── scripts/
    └── generate-docs.py
```

Within each language directory, solutions live in kyu subfolders (`8kyu/`, `7kyu/`, …, `1kyu/`). **A higher kyu number means an easier exercise; a lower kyu means a harder one.**

## File naming

- **One file per kata per language.**
- The filename is the kata slug in kebab-case (for example `array-plus-array.py`).
- The slug should match the Codewars kata URL when possible.

## File headers

Every solution file starts with a short header containing:

| Field | Example |
|-------|---------|
| Title | `Array plus array` |
| Link | `https://www.codewars.com/kata/5a2be17aee1aaefe2a000151` |
| Difficulty | `8 kyu` |
| Description | Problem statement (optional `## Description` heading) |

Use the comment style natural to the language (docstring, `//`, `/* */`, `#`, `--`, etc.).

## Language-specific notes

- **Java / C#:** The public type name may follow the Codewars skeleton (for example class `Sum` in `array-plus-array.java`). The **filename** still uses the kata slug.
- **Go:** Solutions use `package kata` without `func main`.
- **Compiled languages (C, C++, Rust, Java):** Snippets omit an entry point; see [Running locally](RUNNING.md) to exercise them on your machine.

## Adding a solution

1. Create `languages/<language>/<N>kyu/<slug>.<ext>`.
2. Add the standard header (title, link, difficulty, description).
3. Regenerate documentation:

```bash
python3 scripts/generate-docs.py
```

## Documentation

- Solution tables in `catalog/README.md` and each `languages/*/README.md` are **generated**. Edit the marker blocks only by running the script above.
- Run instructions live in [RUNNING.md](RUNNING.md).
