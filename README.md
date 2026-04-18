# Codewars Challenges

A collection of my solutions to [Codewars](https://www.codewars.com/) challenges, organized by language and difficulty.

## Table of contents

- [Codewars Challenges](#codewars-challenges)
  - [Table of contents](#table-of-contents)
  - [Repository layout and conventions](#repository-layout-and-conventions)
    - [Repository layout](#repository-layout)
    - [Conventions](#conventions)
    - [Language documentation](#language-documentation)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
    - [7 kyu](#7-kyu)
    - [6 kyu](#6-kyu)
    - [5 kyu](#5-kyu)
    - [4 kyu](#4-kyu)
    - [3 kyu](#3-kyu)
    - [2 kyu](#2-kyu)
    - [1 kyu](#1-kyu)
  - [License](#license)

## Repository layout and conventions

### Repository layout

```
dsa-codewars/
├── Go/
├── Groovy/
├── JavaScript/
├── Python/
└── README.md
```

Within each language directory, files live in subfolders that reflect difficulty on Codewars (for example `2kyu/`, `3kyu/`, `5kyu/`, `8kyu/`). **A higher kyu means an easier exercise; a lower kyu means a harder one.** Per-language catalogs with every file path live in each language README (see [Language documentation](#language-documentation)).

### Conventions

- One file per exercise; filenames follow the kata slug in kebab-case.
- Each file includes a short header with the title, link to the exercise on Codewars, difficulty, and problem statement.

### Language documentation

- [Go](Go/README.md)
- [Groovy](Groovy/README.md)
- [JavaScript](JavaScript/README.md)
- [Python](Python/README.md)

This repository does not include a shared test runner.

**To run a solution on your machine:**

- **Go:** See [Running locally](Go/README.md#running-locally) — snippets omit `func main`; use `go test`, a small `package main`, or import `kata` in a module.
- **Groovy:** `groovy path/to/kata-file.groovy`, or `groovysh` / `groovy -e` — see [Running locally](Groovy/README.md#running-locally).
- **JavaScript:** `node path/to/kata-file.js` — see [Running locally](JavaScript/README.md#running-locally) (add `console.log(...)` when the file only defines functions).
- **Python:** `python3 path/to/kata-file.py`, or `python3 -i path/to/kata-file.py` — see [Running locally](Python/README.md#running-locally).

The canonical test suite for each exercise is on Codewars, via the link in that file’s header.

## Solutions

**Kyu** levels run from **8 kyu** (easiest) toward **1 kyu** (hardest): a higher kyu number means an easier exercise.

Below, each row lists every implementation in this repo. Language links use paths from the repository root, separated by an em dash (—).

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [JavaScript](JavaScript/8kyu/array-plus-array.js) — [Python](Python/8kyu/array-plus-array.py) |
| Beginner - Lost Without a Map | [Go](Go/8kyu/beginner-lost-without-a-map.go) — [JavaScript](JavaScript/8kyu/beginner-lost-without-a-map.js) — [Python](Python/8kyu/beginner-lost-without-a-map.py) |
| Even or Odd | [Go](Go/8kyu/even-or-odd.go) — [Groovy](Groovy/8kyu/even-or-odd.groovy) — [JavaScript](JavaScript/8kyu/even-or-odd.js) — [Python](Python/8kyu/even-or-odd.py) |
| Find Maximum and Minimum Values of a List | [JavaScript](JavaScript/8kyu/find-maximum-and-minimum-values-of-a-list.js) — [Python](Python/8kyu/find-maximum-and-minimum-values-of-a-list.py) |
| Find the smallest integer in the array | [Groovy](Groovy/8kyu/find-the-smallest-integer-in-the-array.groovy) |
| Grasshopper - Debug | [Groovy](Groovy/8kyu/grasshopper-debug.groovy) — [JavaScript](JavaScript/8kyu/grasshopper-debug.js) — [Python](Python/8kyu/grasshopper-debug.py) |
| If you can't sleep, just count sheep!! | [Go](Go/8kyu/if-you-cant-sleep-just-count-sheep.go) — [JavaScript](JavaScript/8kyu/if-you-cant-sleep-just-count-sheep.js) — [Python](Python/8kyu/if-you-cant-sleep-just-count-sheep.py) |
| Invert Values | [Go](Go/8kyu/invert-values.go) — [JavaScript](JavaScript/8kyu/invert-values.js) — [Python](Python/8kyu/invert-values.py) |
| Sum Arrays | [JavaScript](JavaScript/8kyu/sum-arrays.js) — [Python](Python/8kyu/sum-arrays.py) |

### 7 kyu

| Exercise | File |
|----------|------|
| Anagram Detection | [Groovy](Groovy/7kyu/anagram-detection.groovy) |
| Binary Addition | [Groovy](Groovy/7kyu/binary-addition.groovy) — [JavaScript](JavaScript/7kyu/binary-addition.js) — [Python](Python/7kyu/binary-addition.py) |
| Get the Middle Character | [JavaScript](JavaScript/7kyu/get-the-middle-character.js) |
| You're a square! | [Groovy](Groovy/7kyu/youre-a-square.groovy) |

### 6 kyu

| Exercise | File |
|----------|------|
| Array.diff | [JavaScript](JavaScript/6kyu/array-diff.js) |
| Break CamelCase | [JavaScript](JavaScript/6kyu/break-camelcase.js) |
| Convert string to camel case | [Python](Python/6kyu/convert-string-to-camelcase.py) |
| Counting Duplicates | [Groovy](Groovy/6kyu/counting-duplicates.groovy) |
| Create Phone Number | [JavaScript](JavaScript/6kyu/create-phone-number.js) |
| Duplicate Encoder | [JavaScript](JavaScript/6kyu/duplicate-encoder.js) |
| Tortoise racing | [Go](Go/6kyu/tortoise-racing.go) — [Groovy](Groovy/6kyu/tortoise-racing.groovy) — [JavaScript](JavaScript/6kyu/tortoise-racing.js) — [Python](Python/6kyu/tortoise-racing.py) |

### 5 kyu

| Exercise | File |
|----------|------|
| Calculating with Functions | [JavaScript](JavaScript/5kyu/calculating-with-functions.js) |
| First Non-Repeating Character | [JavaScript](JavaScript/5kyu/first-non-repeating-character.js) |
| Moving Zeros to the End | [JavaScript](JavaScript/5kyu/moving-zeros-to-the-end.js) |
| My smallest code interpreter (aka Brainf**k) | [Groovy](Groovy/5kyu/my-smallest-code-interpreter-aka-brainfk.groovy) — [JavaScript](JavaScript/5kyu/my-smallest-code-interpreter-aka-brainfk.js) — [Python](Python/5kyu/my-smallest-code-interpreter-aka-brainfk.py) |
| Pete, the baker | [Go](Go/5kyu/pete-the-baker.go) — [JavaScript](JavaScript/5kyu/pete-the-baker.js) — [Python](Python/5kyu/pete-the-baker.py) |
| The Hashtag Generator | [Groovy](Groovy/5kyu/the-hashtag-generator.groovy) — [JavaScript](JavaScript/5kyu/the-hashtag-generator.js) — [Python](Python/5kyu/the-hashtag-generator.py) |

### 4 kyu

| Exercise | File |
|----------|------|
| 4 By 4 Skyscrapers | [Go](Go/4kyu/4-by-4-skyscrapers.go) — [JavaScript](JavaScript/4kyu/4-by-4-skyscrapers.js) — [Python](Python/4kyu/4-by-4-skyscrapers.py) |

### 3 kyu

| Exercise | File |
|----------|------|
| Battleship field validator | [Python](Python/3kyu/battleship-field-validator.py) |
| The builder of things | [JavaScript](JavaScript/3kyu/the-builder-of-things.js) — [Python](Python/3kyu/the-builder-of-things.py) |
| The Millionth Fibonacci | [Python](Python/3kyu/the-millionth-fibonacci.py) |

### 2 kyu

| Exercise | File |
|----------|------|
| Linear equations N x M, complete solution space, fraction representation | [JavaScript](JavaScript/2kyu/linear-equations-n-x-m-complete-solution-space-fraction-representation.js) — [Python](Python/2kyu/linear-equations-n-x-m-complete-solution-space-fraction-representation.py) |

### 1 kyu

| Exercise | File |
|----------|------|
| Simple Interactive Interpreter | [JavaScript](JavaScript/1kyu/simple-interactive-nterpreter.js) — [Python](Python/1kyu/simple-interactive-nterpreter.py) |

## License

This repository is **personal practice only**: my own solutions to [Codewars](https://www.codewars.com/) katas, kept for learning and reference. It is **not** affiliated with or endorsed by Codewars.

Exercise descriptions, tests, and trademarks belong to Codewars and the respective kata authors. Code in this repo is shared as-is, without warranty. If you use or adapt anything here, you remain responsible for complying with Codewars’ terms and with any license that applies to the original kata content.
