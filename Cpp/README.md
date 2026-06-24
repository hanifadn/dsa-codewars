# C++

Codewars exercises solved in C++.

## Table of contents

- [C++](#c)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.cpp` file begins with a block comment: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [C++](https://isocpp.org/) with GCC or Clang.
- **Standard:** **C++11** or newer.

Check your toolchain: `g++ --version` or `clang++ --version`

Snippets define functions only (no `main`). To compile locally, add a small `main` that calls the function, or paste the code into the Codewars editor and run tests there.

```bash
g++ -std=c++11 -Wall path/to/kata-file.cpp -o kata && ./kata
```

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.cpp](8kyu/array-plus-array.cpp) |

## License

These C++ files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
