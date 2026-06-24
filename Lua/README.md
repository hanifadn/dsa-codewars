# Lua

Codewars exercises solved in Lua.

## Table of contents

- [Lua](#lua)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.lua` file begins with line comments (`--`): title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [Lua](https://www.lua.org/) — standard library (no extra packages required for these exercises).
- **Lua:** **5.3** or newer (Codewars uses Lua 5.3 per [language docs](https://docs.codewars.com/languages/lua)).

Check your runtime: `lua -v`

```bash
lua path/to/kata-file.lua
```

If the file only defines functions, use the REPL (`lua -i path/to/kata-file.lua`) to call them, or paste the code into the Codewars editor and run tests there.

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.lua](8kyu/array-plus-array.lua) |

## License

These Lua files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
