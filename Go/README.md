# Go

Codewars exercises solved in Go.

## Table of contents

- [Go](#go)
  - [Table of contents](#table-of-contents)
  - [Solutions](#solutions)
    - [4 kyu](#4-kyu)
    - [5 kyu](#5-kyu)
    - [6 kyu](#6-kyu)
  - [Structure](#structure)
  - [File headers](#file-headers)
  - [Running locally](#running-locally)

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 4 kyu

| Exercise | File |
|----------|------|
| 4 By 4 Skyscrapers | [4-by-4-skyscrapers.go](4kyu/4-by-4-skyscrapers.go) |

### 5 kyu

| Exercise | File |
|----------|------|
| Pete, the baker | [pete-the-baker.go](5kyu/pete-the-baker.go) |

### 6 kyu

| Exercise | File |
|----------|------|
| Tortoise racing | [tortoise-racing.go](6kyu/tortoise-racing.go) |

## Structure

Solutions are grouped in subfolders named after Codewars difficulty (for example `4kyu/`). Folder names match the level so you can navigate by kyu.

## File headers

Each `.go` file begins with line comments: title, link to the kata on Codewars, difficulty, and problem description.

## Running locally

- **Tech stack:** [Go](https://go.dev/) — standard library (no extra modules required for these exercises).
- **Go:** **1.18** or newer.

Check your toolchain: `go version`

Solutions use `package kata` where that matches Codewars. There is no `func main` in these files; run tests on Codewars via the link in the header, or add a small `package main` in the same module that imports the kata package and calls its functions, or use a `_test.go` file with `go test`.
