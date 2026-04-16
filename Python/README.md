# Python

Codewars exercises solved in Python.

## Table of contents

- [Python](#python)
  - [Table of contents](#table-of-contents)
  - [Solutions](#solutions)
    - [1 kyu](#1-kyu)
    - [3 kyu](#3-kyu)
    - [4 kyu](#4-kyu)
    - [6 kyu](#6-kyu)
    - [8 kyu](#8-kyu)
  - [Structure](#structure)
  - [File headers](#file-headers)
  - [Running locally](#running-locally)

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 1 kyu

| Exercise | File |
|----------|------|
| Simple Interactive Interpreter | [simple-interactive-nterpreter.py](1kyu/simple-interactive-nterpreter.py) |

### 3 kyu

| Exercise | File |
|----------|------|
| Battleship field validator | [battleship-field-validator.py](3kyu/battleship-field-validator.py) |
| The Millionth Fibonacci | [the-millionth-fibonacci.py](3kyu/the-millionth-fibonacci.py) |

### 4 kyu

| Exercise | File |
|----------|------|
| 4 By 4 Skyscrapers | [4-by-4-skyscrapers.py](4kyu/4-by-4-skyscrapers.py) |

### 6 kyu

| Exercise | File |
|----------|------|
| Convert string to camel case | [convert-string-to-camelcase.py](6kyu/convert-string-to-camelcase.py) |

### 8 kyu

| Exercise | File |
|----------|------|
| Beginner - Lost Without a Map | [beginner-lost-without-a-map.py](8kyu/beginner-lost-without-a-map.py) |
| Find Maximum and Minimum Values of a List | [find-maximum-and-minimum-values-of-a-list.py](8kyu/find-maximum-and-minimum-values-of-a-list.py) |
| If you can't sleep, just count sheeps!! | [if-you-cant-sleep-just-count-sheep.py](8kyu/if-you-cant-sleep-just-count-sheep.py) |
| Invert Values | [invert-values.py](8kyu/invert-values.py) |
| Sum Arrays | [sum-arrays.py](8kyu/sum-arrays.py) |

## Structure

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

## File headers

Each `.py` file begins with a module docstring: title, link to the kata on Codewars, difficulty, and problem description.

## Running locally

- **Tech stack:** [Python](https://www.python.org/) 3 — standard library (no extra packages required for these exercises).
- **Python:** **3.8** or newer.

Check your runtime: `python3 --version` (or `python --version` if that points to Python 3 on your system).

```bash
python3 path/to/kata-file.py
```

If the file only defines functions, use a REPL (`python3 -i path/to/kata-file.py` or `python3 -i`) to import and call them, or paste the code into the Codewars editor and run tests there.