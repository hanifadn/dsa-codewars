# Scala

Codewars exercises solved in Scala.

## Table of contents

- [Scala](#scala)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.scala` file begins with a block comment: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [Scala](https://www.scala-lang.org/) on the JVM — standard library (no extra dependencies required for these exercises).
- **Scala:** **2.13** or newer (Codewars uses Scala 2.13 per [language docs](https://docs.codewars.com/languages/scala)).

Check your runtime: `scala -version`

Snippets define methods on a `Kata` object (no `App` or `main`). To run locally, use the REPL (`scala -i path/to/kata-file.scala`) or paste the code into the Codewars editor and run tests there.

```bash
scala path/to/kata-file.scala
```

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an easier exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.scala](8kyu/array-plus-array.scala) |

## License

These Scala files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
