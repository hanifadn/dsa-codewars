# Even or Odd

| Field | Value |
|-------|-------|
| Slug | even-or-odd |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/53da3dbb4a5168369a0000fe |
| Status | backfilled |
| Reference | languages/python/8kyu/even-or-odd.py |

## Summary

Given an integer, return the string `"Even"` if the number is even, or `"Odd"` if it is odd. Zero is even.

## Input / Output

- **Input:** A single integer.
- **Output:** The string `"Even"` or `"Odd"` (exact casing).
- **Constraints:** Standard integer parity rules apply; negative integers are supported.

## Examples

| Input | Output |
|-------|--------|
| `0` | `"Even"` |
| `2` | `"Even"` |
| `3` | `"Odd"` |
| `-4` | `"Even"` |
| `-7` | `"Odd"` |

## Edge Cases

- Zero → `"Even"`.
- Negative even/odd integers follow the same modulo-2 rule.
- Large magnitudes still reduce to parity via modulo 2.

## Approach

- **Algorithm:** Check whether `number % 2 == 0`; return `"Even"` if true, otherwise `"Odd"`.
- **Time:** O(1).
- **Space:** O(1).

## Behavioral Contract

- Return exactly `"Even"` or `"Odd"` — no lowercase or numeric output.
- Zero is even.
- Sign does not affect parity.

## Pseudocode

```text
FUNCTION even_or_odd(number):
  IF number MOD 2 == 0:
    RETURN "Even"
  ELSE:
    RETURN "Odd"
```

## Walkthrough

For `number = 3`:

1. Compute `3 % 2 = 1` (not zero).
2. Condition is false → return `"Odd"`.

For `number = -4`:

1. Compute `-4 % 2 = 0`.
2. Condition is true → return `"Even"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `func EvenOrOdd(number int) string` | Modulo-2 branch |
| Groovy | `static evenOrOdd(number)` | Ternary on `number % 2` |
| JavaScript | `function evenOrOdd(number)` | Modulo check, return string literal |
| Python | `def even_or_odd(number: int) -> str` | Ternary on `number % 2 == 0` |
