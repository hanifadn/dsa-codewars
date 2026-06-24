# C#

Codewars exercises solved in C#.

## Table of contents

- [C#](#c)
  - [Table of contents](#table-of-contents)
  - [File format and local runs](#file-format-and-local-runs)
    - [File headers](#file-headers)
    - [Running locally](#running-locally)
  - [Solutions](#solutions)
    - [8 kyu](#8-kyu)
  - [License](#license)

## File format and local runs

### File headers

Each `.cs` file begins with a block comment: title, link to the kata on Codewars, difficulty, and problem description.

Solutions are grouped in subfolders named after Codewars difficulty (for example `8kyu/`). Folder names match the level so you can navigate by kyu.

### Running locally

**To run a solution on your machine:**

- **Tech stack:** [.NET SDK](https://dotnet.microsoft.com/) or the `csc` compiler from the .NET Framework / Mono.
- **.NET:** **6** or newer recommended.

Check your toolchain: `dotnet --version`

Snippets define static methods on a `Kata` class (no entry point). To run locally, wrap the file in a small console project or paste the code into the Codewars editor and run tests there.

```bash
dotnet new console -o kata-run && cp path/to/kata-file.cs kata-run/Program.cs && dotnet run --project kata-run
```

## Solutions

**Kyu** levels on Codewars run from **8 kyu** (easiest) toward **1 kyu** (hardest): a **higher** kyu number means an **easier** exercise; a **lower** kyu number means a **harder** one.

### 8 kyu

| Exercise | File |
|----------|------|
| Array Plus Array | [array-plus-array.cs](8kyu/array-plus-array.cs) |

## License

These C# files are **personal practice solutions** only — not affiliated with [Codewars](https://www.codewars.com/). For the full notice, see [License](../README.md#license) in the repository root.
