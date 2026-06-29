# Binary Addition

| Field | Value |
|-------|-------|
| Slug | binary-addition |
| Kyu | 7 |
| Link | https://www.codewars.com/kata/551f37452ff852b7bd000139 |
| Status | backfilled |
| Reference | languages/python/7kyu/binary-addition.py |

## Summary

Add two integers and return their sum encoded as a binary string without a `0b` prefix.

## Input / Output

- **Input:** Two integers `a` and `b`.
- **Output:** A string of `'0'` and `'1'` characters representing `(a + b)` in base 2.
- **Constraints:** Use standard integer addition; convert the sum to binary text only (no radix prefix).

## Examples

| Input | Output |
|-------|--------|
| `1`, `1` | `"10"` |
| `5`, `9` | `"1110"` |
| `0`, `0` | `"0"` |

## Edge Cases

- Zero sum → `"0"`.
- Large values that still fit in the kata's integer type.
- Negative sums (if the kata allows signed inputs) must use the platform's binary conversion rules.

## Approach

- **Algorithm:** Compute `sum = a + b`, then convert `sum` to a base-2 string with no prefix.
- **Time:** O(log sum) digits in the result.
- **Space:** O(log sum) for the output string.

## Behavioral Contract

- Return type is string, not numeric.
- No `0b` / `0B` prefix in the result.
- Leading zeros are omitted except for the single digit `"0"`.

## Pseudocode

```text
FUNCTION addBinary(a, b):
  sum = a + b
  RETURN BINARY_STRING(sum) WITHOUT RADIX PREFIX
```

## Walkthrough

For `a = 5`, `b = 9`:

1. `sum = 14`.
2. Binary of 14 is `1110`.
3. Return `"1110"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static String addBinary(long a, long b)` | `Long.toBinaryString(a + b)` |
| JavaScript | `function addBinary(a, b)` | `(a + b).toString(2)` |
| Python | `def add_binary(a: int, b: int) -> str` | `bin(a + b)[2:]` strips `0b` |
