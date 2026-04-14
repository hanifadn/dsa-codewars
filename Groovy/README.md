# Groovy

Codewars exercises solved in Groovy.

## Table of contents

- [Groovy](#groovy)
  - [Table of contents](#table-of-contents)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
    - [7 kyu](#7-kyu)
    - [6 kyu](#6-kyu)
  - [Structure](#structure)
  - [File headers](#file-headers)
  - [Running locally](#running-locally)

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Find the smallest integer in the array | [find-the-smallest-integer-in-the-array.groovy](8kyu/find-the-smallest-integer-in-the-array.groovy) |

### 7 kyu

| Exercise | File |
|----------|------|
| Anagram Detection | [anagram-detection.groovy](7kyu/anagram-detection.groovy) |
| You're a square! | [youre-a-square.groovy](7kyu/youre-a-square.groovy) |

### 6 kyu

| Exercise | File |
|----------|------|
| Counting Duplicates | [counting-duplicates.groovy](6kyu/counting-duplicates.groovy) |

## Structure

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`, `7kyu/`). Folder names match the level so you can navigate by kyu.

## File headers

Each `.groovy` file begins with a block comment: title, link to the kata on Codewars, difficulty, and problem description.

## Running locally

- **Tech stack:** [Apache Groovy](https://groovy-lang.org/) on the JVM — standard library; no extra packages required for these exercises.
- **Groovy:** **2.5** or newer (Codewars uses Groovy 2.5 per [language docs](https://docs.codewars.com/languages/groovy); newer versions usually work for the same snippets).

Check your runtime: `groovy --version`

```bash
groovy path/to/kata-file.groovy
```

To compile without running: `groovyc path/to/kata-file.groovy`

If the file only defines classes or functions, use `groovy -e '...'` for a quick snippet, open a REPL (`groovysh`), or paste the code into the Codewars editor and run tests there.