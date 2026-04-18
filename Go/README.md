# Go

Codewars exercises solved in Go.

## Table of contents

- [Go](#go)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
    - [6 kyu](#6-kyu)
    - [5 kyu](#5-kyu)
    - [4 kyu](#4-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.go` file begins with line comments: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`, `4kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [Go](https://go.dev/) — standard library (no extra modules required for these exercises).
- **Go:** **1.18** or newer.

Check your toolchain: `go version`

Solutions use `package kata` where that matches Codewars. There is no `func main` in these files; run tests on Codewars via the link in the header, or add a small `package main` in the same module that imports the kata package and calls its functions, or use a `_test.go` file with `go test`.

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Beginner - Lost Without a Map | [beginner-lost-without-a-map.go](8kyu/beginner-lost-without-a-map.go) |
| Even or Odd | [even-or-odd.go](8kyu/even-or-odd.go) |
| If you can't sleep, just count sheep!! | [if-you-cant-sleep-just-count-sheep.go](8kyu/if-you-cant-sleep-just-count-sheep.go) |
| Invert values | [invert-values.go](8kyu/invert-values.go) |

### 6 kyu

| Exercise | File |
|----------|------|
| Tortoise racing | [tortoise-racing.go](6kyu/tortoise-racing.go) |

### 5 kyu

| Exercise | File |
|----------|------|
| Pete, the baker | [pete-the-baker.go](5kyu/pete-the-baker.go) |

### 4 kyu

| Exercise | File |
|----------|------|
| 4 By 4 Skyscrapers | [4-by-4-skyscrapers.go](4kyu/4-by-4-skyscrapers.go) |

## License

These Go files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
