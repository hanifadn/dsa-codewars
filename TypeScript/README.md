# TypeScript

Codewars exercises solved in TypeScript.

## Table of contents

- [TypeScript](#typescript)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.ts` file begins with a JSDoc-style block: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [TypeScript](https://www.typescriptlang.org/) with [Node.js](https://nodejs.org/) or `tsx`.
- **TypeScript:** **5.x** recommended; **Node.js 18.x** or newer.

Check your toolchain: `tsc --version` and `node --version`

Snippets export functions only (no entry point). Compile and run with `tsc` + `node`, use `tsx` for a one-step run, or paste the code into the Codewars editor and run tests there.

```bash
npx tsx path/to/kata-file.ts
```

Or compile first:

```bash
tsc path/to/kata-file.ts && node path/to/kata-file.js
```

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.ts](8kyu/array-plus-array.ts) |

## License

These TypeScript files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
