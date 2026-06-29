# Invert values

| Field | Value |
|-------|-------|
| Slug | invert-values |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad |
| Status | backfilled |
| Reference | languages/python/8kyu/invert-values.py |

## Summary

Given an array of integers, return a new array where each value is replaced by its additive inverse (negation). Positives become negative and negatives become positive. Do not mutate the input array.

## Input / Output

- **Input:** An array of integers (possibly empty).
- **Output:** A new array of the same length with each element negated.
- **Constraints:** All values are integers; input must not be modified in place.

## Examples

| Input | Output |
|-------|--------|
| `[1, 2, 3, 4, 5]` | `[-1, -2, -3, -4, -5]` |
| `[1, -2, 3, -4, 5]` | `[-1, 2, -3, 4, -5]` |
| `[]` | `[]` |
| `[0]` | `[0]` |

## Edge Cases

- Empty array → empty result.
- Zero negates to zero.
- Mixed positive and negative values swap signs.

## Approach

- **Algorithm:** Map each element to its negation and collect into a new array.
- **Time:** O(n), where n is array length.
- **Space:** O(n) for the output array.

## Behavioral Contract

- Return a new array; never mutate the input.
- Negation is additive inverse: `-(x)`.
- Preserve element order.
- Empty input → empty output.

## Pseudocode

```text
FUNCTION invert(lst):
  result = NEW EMPTY ARRAY
  FOR EACH num IN lst:
    APPEND (-num) TO result
  RETURN result
```

## Walkthrough

For `lst = [1, -2, 3, -4, 5]`:

1. Negate `1` → `-1`.
2. Negate `-2` → `2`.
3. Negate `3` → `-3`.
4. Negate `-4` → `4`.
5. Negate `5` → `-5`.
6. Return `[-1, 2, -3, 4, -5]`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `func Invert(arr []int) []int` | New slice, `-v` per element |
| JavaScript | `function invert(array)` | `array.map(n => -n)` |
| Python | `def invert(lst)` | `[-num for num in lst]` |
