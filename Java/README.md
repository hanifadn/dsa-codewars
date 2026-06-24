# Java

Codewars exercises solved in Java.

## Table of contents

- [Java](#java)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.java` file begins with a Javadoc-style block: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [OpenJDK](https://openjdk.org/) or another Java SE distribution.
- **Java:** **11** or newer.

Check your runtime: `java -version` and `javac -version`

Snippets use a `Sum` class (or similar Codewars skeleton) with static methods (no `main`). To run locally, add a temporary `main` or paste into the Codewars editor.

```bash
javac path/to/Sum.java && java -cp path/to Sum
```

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.java](8kyu/array-plus-array.java) |

## License

These Java files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
