# Beginner - Lost Without a Map

| Field | Value |
|-------|-------|
| Slug | beginner-lost-without-a-map |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/57f781872e3d8ca2a000007e |
| Status | backfilled |
| Reference | languages/python/8kyu/beginner-lost-without-a-map.py |

## Summary

Given an array of integers, return a new array where every element is doubled (multiplied by 2). The original array must remain unchanged.

## Input / Output

- **Input:** An array of integers.
- **Output:** A new array of the same length with each value multiplied by 2.
- **Constraints:** Elements are integers; the input array may be empty.

## Examples

| Input | Output |
|-------|--------|
| `[1, 2, 3]` | `[2, 4, 6]` |
| `[0, 1, 2, 3]` | `[0, 2, 4, 6]` |
| `[]` | `[]` |
| `[-1, -2]` | `[-2, -4]` |

## Edge Cases

- Empty array → empty result array.
- Zeros remain zero after doubling.
- Negative values become more negative.

## Approach

- **Algorithm:** Map each element to `element * 2` and collect into a new array.
- **Time:** O(n), where n is the array length.
- **Space:** O(n) for the new output array.

## Behavioral Contract

- Return a new array; do not mutate the input array.
- Preserve element order.
- Empty input → empty output (not `null`/`nil` unless the language API requires otherwise).

## Pseudocode

```text
FUNCTION maps(a):
  result = NEW EMPTY ARRAY
  FOR EACH num IN a:
    APPEND (num * 2) TO result
  RETURN result
```

## Walkthrough

For `a = [1, 2, 3]`:

1. Initialize `result = []`.
2. Process `1` → append `2`.
3. Process `2` → append `4`.
4. Process `3` → append `6`.
5. Return `[2, 4, 6]`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `func Maps(arr []int) []int` | Allocates new slice, doubles each element |
| JavaScript | `function maps(x)` | `x.map(n => n * 2)` |
| Python | `def maps(a)` | List comprehension `[num * 2 for num in a]` |
