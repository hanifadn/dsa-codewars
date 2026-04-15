# Codewars Challenges

A collection of my solutions to [Codewars](https://www.codewars.com/) challenges, organized by language and difficulty.

## Table of contents

- [Codewars Challenges](#codewars-challenges)
  - [Table of contents](#table-of-contents)
  - [Solutions](#solutions)
  - [Repository layout](#repository-layout)
  - [Conventions](#conventions)
  - [Running solutions locally](#running-solutions-locally)
  - [Language documentation](#language-documentation)

## Solutions

Exercise catalogs grouped by level (**8 kyu** → **1 kyu**: higher kyu = easier, lower kyu = harder):

- [Go — Solutions](Go/README.md#solutions)
- [Groovy — Solutions](Groovy/README.md#solutions)
- [JavaScript — Solutions](JavaScript/README.md#solutions)
- [Python — Solutions](Python/README.md#solutions)

## Repository layout

```
codewars-challenges/
├── Go/
├── Groovy/
├── JavaScript/
├── Python/
└── README.md
```

Within each language directory, files live in subfolders that reflect difficulty on Codewars. **A higher kyu means an easier exercise; a lower kyu means a harder one.** See the language READMEs above for full listings.

## Conventions

- One file per exercise; filenames follow the kata slug in kebab-case.
- Each file includes a short header with the title, link to the exercise on Codewars, difficulty, and problem statement.

## Running solutions locally

This repository does not include a shared test runner. To run a solution on your machine:

- **Go:** `go test` in a module that contains the kata, or a small `package main` that imports `kata` and calls the solution; see [Go/README.md](Go/README.md#running-locally).
- **Groovy:** `groovy path/to/file.groovy`, or use `groovysh` / a small `groovy -e` script if the file only defines classes.
- **JavaScript:** `node path/to/file.js` (add a `console.log` if the file only defines functions).
- **Python:** `python path/to/file.py` or use a REPL to import and call the functions.

The canonical test suite for each exercise is on Codewars, via the link in that file’s header.

## Language documentation

- [Go](Go/README.md)
- [Groovy](Groovy/README.md)
- [JavaScript](JavaScript/README.md)
- [Python](Python/README.md)