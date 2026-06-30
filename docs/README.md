# Documentation

Three layers under `docs/`:

| Layer | Path | Role |
|-------|------|------|
| **Guide** | [guide/](guide/) | How to work with the repo (hand-authored) |
| **Catalog** | [catalog/](catalog/) | Solution index from code (generated) |
| **Logic** | [logic/](logic/) | Kata specs and pseudocode (hand-authored + generated index) |

## Quick links

| | |
|---|---|
| [Solution catalog](catalog/README.md) | 33 katas · 87 solutions · 16 languages |
| [Logic index](logic/README.md) | 33 behavioral contracts |
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
