# JavaScript

Codewars exercises solved in JavaScript.

## Table of contents

- [JavaScript](#javascript)
  - [Table of contents](#table-of-contents)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
    - [7 kyu](#7-kyu)
    - [6 kyu](#6-kyu)
    - [5 kyu](#5-kyu)
    - [4 kyu](#4-kyu)
    - [1 kyu](#1-kyu)
  - [Structure](#structure)
  - [File headers](#file-headers)
  - [Running locally](#running-locally)

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Even or Odd | [even-or-odd.js](8kyu/even-or-odd.js) |

### 7 kyu

| Exercise | File |
|----------|------|
| Binary Addition | [binary-addition.js](7kyu/binary-addition.js) |
| Get the Middle Character | [get-the-middle-character.js](7kyu/get-the-middle-character.js) |

### 6 kyu

| Exercise | File |
|----------|------|
| Array.diff | [array-diff.js](6kyu/array-diff.js) |
| Break CamelCase | [break-camelcase.js](6kyu/break-camelcase.js) |
| Create Phone Number | [create-phone-number.js](6kyu/create-phone-number.js) |
| Duplicate Encoder | [duplicate-encoder.js](6kyu/duplicate-encoder.js) |

### 5 kyu

| Exercise | File |
|----------|------|
| Calculating with Functions | [calculating-with-functions.js](5kyu/calculating-with-functions.js) |
| First Non-Repeating Character | [first-non-repeating-character.js](5kyu/first-non-repeating-character.js) |
| Moving Zeros to the End | [moving-zeros-to-the-end.js](5kyu/moving-zeros-to-the-end.js) |

### 4 kyu

| Exercise | File |
|----------|------|
| 4 By 4 Skyscrapers | [4-by-4-skyscrapers.js](4kyu/4-by-4-skyscrapers.js) |

### 1 kyu

| Exercise | File |
|----------|------|
| Simple Interactive Interpreter | [simple-interactive-nterpreter.js](1kyu/simple-interactive-nterpreter.js) |

## Structure

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`, `7kyu/`). Folder names match the level so you can navigate by kyu.

## File headers

Each `.js` file begins with a JSDoc-style block: title, link to the kata on Codewars, difficulty, and problem description.

## Running locally

- **Tech stack:** [Node.js](https://nodejs.org/) — vanilla JavaScript (no framework or bundler).
- **Node.js:** **18.x** or newer (current [LTS](https://nodejs.org/en/about/previous-releases) recommended).

Check your runtime: `node --version`

```bash
node path/to/kata-file.js
```

If the file only defines functions, add a temporary `console.log(...)` to exercise them, or paste the code into the Codewars editor and run tests there.