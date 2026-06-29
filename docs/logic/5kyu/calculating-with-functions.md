# Calculating with Functions

| Field | Value |
|-------|-------|
| Slug | calculating-with-functions |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/5259121576d2994056000521 |
| Status | backfilled |
| Reference | languages/javascript/5kyu/calculating-with-functions.js |

## Summary

Implement digit functions `zero` through `nine` and operation helpers `plus`, `minus`, `times`, and `dividedBy` so that nested calls like `seven(times(five()))` evaluate a single binary operation. The outer digit is the left operand; the inner digit (wrapped by the operation) is the right operand.

## Input / Output

- **Input:** Nested calls of the form `DIGIT(OPERATION(DIGIT()))` where each digit function may be called with zero or one argument.
- **Output:** The integer result of applying the operation to the two operands.
- **Constraints:** Exactly one operation and two numbers per expression; division is integer (floor) division.

## Examples

| Input | Output |
|-------|--------|
| `seven(times(five()))` | 35 |
| `four(plus(nine()))` | 13 |
| `eight(minus(three()))` | 5 |
| `six(dividedBy(two()))` | 3 |
| `eight(dividedBy(three()))` | 2 |

## Edge Cases

- Digit called with no argument returns its numeric value (e.g. `five()` → 5).
- Division truncates toward negative infinity (floor), not toward zero.
- Operands are always integers 0–9.

## Approach

- **Algorithm:** Curried higher-order functions. Each operation `op(b)` returns a unary function `a ↦ result`. Each digit `n(fn)` returns `fn(n)` when `fn` is provided, else `n`.
- **Time:** O(1)
- **Space:** O(1)

## Behavioral Contract

- `plus(b)(a) = a + b`, `minus(b)(a) = a - b`, `times(b)(a) = a * b`, `dividedBy(b)(a) = floor(a / b)`.
- Evaluation order: inner digit resolves to right operand; outer digit passes left operand into the operation closure.
- No side effects; pure functions.

## Pseudocode

```text
FUNCTION digit(n, optional op):
  IF op IS PROVIDED:
    RETURN op(n)
  RETURN n

FUNCTION plus(b):
  RETURN LAMBDA a: a + b

FUNCTION minus(b):
  RETURN LAMBDA a: a - b

FUNCTION times(b):
  RETURN LAMBDA a: a * b

FUNCTION dividedBy(b):
  RETURN LAMBDA a: FLOOR(a / b)

// zero..nine are digit(0)..digit(9)
```

## Walkthrough

For `seven(times(five()))`:

1. `five()` with no op → 5.
2. `times(5)` returns `λa. a * 5`.
3. `seven(that_fn)` → `that_fn(7)` → `7 * 5` → **35**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `zero` … `nine`, `plus`, `minus`, `times`, `dividedBy` | Curried closures |
