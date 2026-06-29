# Running locally

This repository does not include a shared test runner. The canonical test suite for each exercise is on Codewars, via the link in that file's header.

<h2 id="c">C</h2>

- **Stack:** [C](https://en.cppreference.com/w/c) with GCC or Clang (**C99** or newer).
- **Check:** `gcc --version` or `clang --version`
- Snippets define functions only (no `main`). Add a temporary `main` to compile locally, or paste into Codewars.

```bash
gcc -std=c99 -Wall path/to/kata-file.c -o kata && ./kata
```

<h2 id="cpp">C++</h2>

- **Stack:** [C++](https://isocpp.org/) with GCC or Clang (**C++11** or newer).
- **Check:** `g++ --version` or `clang++ --version`
- Add a temporary `main` to compile locally, or paste into Codewars.

```bash
g++ -std=c++11 -Wall path/to/kata-file.cpp -o kata && ./kata
```

<h2 id="csharp">C#</h2>

- **Stack:** [.NET SDK](https://dotnet.microsoft.com/) **6** or newer.
- **Check:** `dotnet --version`
- Wrap the snippet in a small console project or paste into Codewars.

```bash
dotnet new console -o kata-run && cp path/to/kata-file.cs kata-run/Program.cs && dotnet run --project kata-run
```

## Dart

- **Stack:** [Dart SDK](https://dart.dev/) **2.19** or newer.
- **Check:** `dart --version`
- Add a temporary `main` if the file only defines functions.

```bash
dart path/to/kata-file.dart
```

## Go

- **Stack:** [Go](https://go.dev/) **1.18** or newer.
- **Check:** `go version`
- Solutions use `package kata` without `func main`. Use `go test`, a small `package main` wrapper, or paste into Codewars.

## Groovy

- **Stack:** [Apache Groovy](https://groovy-lang.org/) **2.5** or newer on the JVM.
- **Check:** `groovy --version`

```bash
groovy path/to/kata-file.groovy
```

Use `groovysh`, `groovy -e`, or paste into Codewars for snippets without a script entry point.

## Java

- **Stack:** [OpenJDK](https://openjdk.org/) or another Java SE distribution (**11** or newer).
- **Check:** `java -version` and `javac -version`
- Snippets use a Codewars skeleton class with static methods (no `main`). Add a temporary `main` or paste into Codewars.

```bash
javac path/to/kata-file.java && java -cp path/to Sum
```

Replace `Sum` with the public class name in that file.

## JavaScript

- **Stack:** [Node.js](https://nodejs.org/) **18.x** or newer (LTS recommended).
- **Check:** `node --version`

```bash
node path/to/kata-file.js
```

Add `console.log(...)` when the file only defines functions.

## Kotlin

- **Stack:** [Kotlin](https://kotlinlang.org/) **1.8** or newer on the JVM.
- **Check:** `kotlinc -version`
- Snippets define top-level functions only (no `main`). Add a temporary `main` or paste into Codewars.

```bash
kotlinc path/to/kata-file.kt -include-runtime -d kata.jar && java -jar kata.jar
```

## Lua

- **Stack:** [Lua](https://www.lua.org/) **5.3** or newer.
- **Check:** `lua -v`

```bash
lua path/to/kata-file.lua
```

Use `lua -i` for a REPL session with the file loaded.

## PHP

- **Stack:** [PHP](https://www.php.net/) **8.0** or newer.
- **Check:** `php --version`

```bash
php path/to/kata-file.php
```

## Python

- **Stack:** [Python](https://www.python.org/) **3.8** or newer.
- **Check:** `python3 --version`

```bash
python3 path/to/kata-file.py
```

Use `python3 -i path/to/kata-file.py` when the file only defines functions.

## Ruby

- **Stack:** [Ruby](https://www.ruby-lang.org/) **2.7** or newer (**3.x** recommended).
- **Check:** `ruby --version`

```bash
ruby path/to/kata-file.rb
```

Use `irb` with `load "path/to/kata-file.rb"` for method-only files.

## Rust

- **Stack:** [Rust](https://www.rust-lang.org/) **1.70** or newer (edition **2021**).
- **Check:** `rustc --version`

```bash
rustc path/to/kata-file.rs -o kata && ./kata
```

For larger exercises, use a temporary Cargo project.

## Scala

- **Stack:** [Scala](https://www.scala-lang.org/) **2.13** or newer on the JVM.
- **Check:** `scala -version`

```bash
scala path/to/kata-file.scala
```

## TypeScript

- **Stack:** [TypeScript](https://www.typescriptlang.org/) **5.x** with [Node.js](https://nodejs.org/) **18.x** or newer.
- **Check:** `tsc --version` and `node --version`

```bash
npx tsx path/to/kata-file.ts
```

Or compile first:

```bash
tsc path/to/kata-file.ts && node path/to/kata-file.js
```
