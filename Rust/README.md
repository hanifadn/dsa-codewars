# Rust

Codewars exercises solved in Rust.

## Table of contents

- [Rust](#rust)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.rs` file begins with line comments (`//`): title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [Rust](https://www.rust-lang.org/) — standard library (no extra crates required for these exercises).
- **Rust:** **1.70** or newer (edition **2021**).

Check your toolchain: `rustc --version`

Snippets define functions only (no `main`). To run locally, add a small `main` in a scratch project or use `cargo test`, or paste the code into the Codewars editor and run tests there.

```bash
rustc path/to/kata-file.rs -o kata && ./kata
```

For multi-file exercises, prefer a temporary Cargo project: `cargo new kata-run && cp path/to/kata-file.rs kata-run/src/lib.rs`.

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.rs](8kyu/array-plus-array.rs) |

## License

These Rust files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
