# Simple Interactive Interpreter

| Field | Value |
|-------|-------|
| Slug | simple-interactive-nterpreter |
| Kyu | 1 |
| Link | https://www.codewars.com/kata/52ffcfa4aff455b3c2000750 |
| Status | backfilled |
| Reference | languages/python/1kyu/simple-interactive-nterpreter.py |

## Summary

Build a stateful expression interpreter supporting variables, right-associative assignment, user-defined functions (`fn name args => body`), and operator precedence. Each `input` call evaluates one expression (or defines a function) using persistent global variables and functions. Division is floating-point; `%` is modulo.

## Input / Output

- **Input:** String expression per `input()` call; interpreter retains state across calls.
- **Output:** Evaluated value for expressions; `""` for successful `fn` definitions; error strings starting with `ERROR:` on failure (interpreter remains usable).
- **Constraints:** No `eval`; function bodies may only reference parameters and other defined functions.

## Examples

| Input | Output |
|-------|--------|
| `x = 7` | `7` |
| `x + 6` (after above) | `13` |
| `fn avg x y => (x + y) / 2` then `avg 2 4` | `3` |
| `y + 7` (y undefined) | `ERROR: Invalid identifier. No variable with name 'y' was found.` |
| `x = y = 7` | `7` |

## Edge Cases

- Empty input → `""`.
- Integer literals without `.` → int; with `.` → float.
- Assignment to name that is an existing function → error.
- Function definition when name is existing variable → error.
- Duplicate parameter names in `fn` → error.
- Unbound identifier in function body at define time → error.
- Function calls are right-associative: `add echo 4 echo 3` → `add(echo(4), echo(3))`.
- Parentheses and nested assignment inside expressions.

## Approach

- **Algorithm:** Regex tokenizer; recursive-descent parser with precedence levels (assignment → additive → multiplicative → primary). Functions stored as (arg names, tokenized body); calls bind locals and parse body in nested parser. Globals: `vars` map and `functions` map.
- **Time:** O(tokens) per input
- **Space:** O(tokens + state)

## Behavioral Contract

- Precedence (low to high): `=`, `+`/`-`, `*`/`/`/`%`; function application binds tighter via primary resolution.
- Assignment: identifier `=` expression (right-associative); stores in global `vars`, returns stored value.
- `fn name arg1 arg2 => body`: body is remaining tokens; validate identifiers in body ⊆ args ∪ function names; store definition; return `""`.
- Lookup order in expressions: local args → global vars → function call if name is function.
- Binary ops: `+ - * / %` with float division for `/`.

## Pseudocode

```text
CLASS Interpreter:
  vars = {}
  functions = {}

  FUNCTION input(expression):
    tokens = tokenize(expression)
    IF tokens empty: RETURN ""
    IF tokens[0] == "fn":
      RETURN defineFunction(tokens)
    parser = ExpressionParser(self, tokens, locals={})
    RETURN parser.parse()

  FUNCTION defineFunction(tokens):
    parse name, argNames, body tokens after "=>"
    IF name in vars: ERROR cannot overwrite variable
    IF duplicate argNames: ERROR
    FOR each identifier token in body:
      IF not arg and not known function: ERROR invalid identifier in body
    functions[name] = (argNames, body)
    RETURN ""

CLASS ExpressionParser(interpreter, tokens, locals):
  pos = 0

  FUNCTION parse():
    result = parseAssignment()
    REQUIRE pos == end
    RETURN result

  FUNCTION parseAssignment():
    IF at pattern IDENT "=":
      name = consume ident; consume "="
      IF name is function: ERROR
      value = parseAssignment()
      interpreter.vars[name] = value
      RETURN value
    RETURN parseAdditive()

  FUNCTION parseAdditive():
    left = parseMultiplicative()
    WHILE peek in {+, -}:
      op = consume; right = parseMultiplicative()
      left = applyBinary(op, left, right)
    RETURN left

  FUNCTION parseMultiplicative():
    left = parsePrimary()
    WHILE peek in {*, /, %}:
      op = consume; right = parsePrimary()
      left = applyBinary(op, left, right)
    RETURN left

  FUNCTION parsePrimary():
    IF number: RETURN parse int or float
    IF "(": consume; val = parseAssignment(); consume ")"; RETURN val
    IF ident:
      IF in locals: RETURN locals[ident]
      IF in interpreter.vars: RETURN vars[ident]
      IF in interpreter.functions:
        consume ident
        args = [parseAssignment() for each formal]
        inner = ExpressionParser(interpreter, body tokens, zip(formals, args))
        RETURN inner.parse()
      ERROR undefined variable
    ERROR syntax

FUNCTION tokenize(s):
  RETURN regex tokens: =>, operators, parens, identifiers, numbers
```

## Walkthrough

`x = 13 + (y = 3)`:

1. Assignment to `x`; RHS is `13 + (y = 3)`.
2. Inner assignment sets `y=3`, returns 3.
3. `13 + 3` → 16; store `x=16`; return **16**.

`fn echo x => x` then `add echo 4 echo 3` with `fn add x y => x + y`:

1. `echo 4` parses as call → 4; `echo 3` → 3; `add(4,3)` → **7**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `Interpreter` / `input` | Recursive descent |
| Python | `Interpreter.input(expression)` | Tokenizer + parser |
