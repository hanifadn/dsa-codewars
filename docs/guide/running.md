# Running locally

No shared test runner — the canonical suite is on Codewars (link in each file header).

[← Documentation](../README.md)

<h2 id="c">C</h2>

Stack: GCC or Clang, **C99+** · `gcc --version`

Snippets omit `main`. Add one locally or paste into Codewars.

```bash
gcc -std=c99 -Wall path/to/kata.c -o kata && ./kata
```

<h2 id="cpp">C++</h2>

Stack: GCC or Clang, **C++11+** · `g++ --version`

```bash
g++ -std=c++11 -Wall path/to/kata.cpp -o kata && ./kata
```

<h2 id="csharp">C#</h2>

Stack: [.NET SDK](https://dotnet.microsoft.com/) **6+** · `dotnet --version`

```bash
dotnet new console -o kata-run && cp path/to/kata.cs kata-run/Program.cs && dotnet run --project kata-run
```

<h2 id="dart">Dart</h2>

Stack: [Dart SDK](https://dart.dev/) **2.19+** · `dart --version`

```bash
dart path/to/kata.dart
```

<h2 id="go">Go</h2>

Stack: [Go](https://go.dev/) **1.18+** · `go version`

Solutions use `package kata` without `main`. Use a wrapper, `go test`, or paste into Codewars.

<h2 id="groovy">Groovy</h2>

Stack: [Groovy](https://groovy-lang.org/) **2.5+** on JVM · `groovy --version`

```bash
groovy path/to/kata.groovy
```

<h2 id="java">Java</h2>

Stack: **Java 11+** · `javac -version`

Replace `Sum` with the public class name in the file.

```bash
javac path/to/kata.java && java -cp path/to Sum
```

<h2 id="javascript">JavaScript</h2>

Stack: [Node.js](https://nodejs.org/) **18+** · `node --version`

```bash
node path/to/kata.js
```

<h2 id="kotlin">Kotlin</h2>

Stack: **Kotlin 1.8+** on JVM · `kotlinc -version`

```bash
kotlinc path/to/kata.kt -include-runtime -d kata.jar && java -jar kata.jar
```

<h2 id="lua">Lua</h2>

Stack: **Lua 5.3+** · `lua -v`

```bash
lua path/to/kata.lua
```

<h2 id="php">PHP</h2>

Stack: **PHP 8.0+** · `php --version`

```bash
php path/to/kata.php
```

<h2 id="python">Python</h2>

Stack: **Python 3.8+** · `python3 --version`

```bash
python3 path/to/kata.py
```

<h2 id="ruby">Ruby</h2>

Stack: **Ruby 2.7+** · `ruby --version`

```bash
ruby path/to/kata.rb
```

<h2 id="rust">Rust</h2>

Stack: **Rust 1.70+** (edition 2021) · `rustc --version`

```bash
rustc path/to/kata.rs -o kata && ./kata
```

<h2 id="scala">Scala</h2>

Stack: **Scala 2.13+** on JVM · `scala -version`

```bash
scala path/to/kata.scala
```

<h2 id="typescript">TypeScript</h2>

Stack: **TypeScript 5.x** + Node **18+** · `npx tsx` or `tsc`

```bash
npx tsx path/to/kata.ts
```

<h2 id="shell">Shell</h2>

Stack: Bash or POSIX shell · `bash --version`

Input via `$1`, output via `echo`.

```bash
bash path/to/kata.sh 4
```

<h2 id="sql">SQL</h2>

Stack: SQLite (Codewars SQL katas) · `sqlite3 --version`

```bash
sqlite3 :memory: < path/to/kata.sql
```
