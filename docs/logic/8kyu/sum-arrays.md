# Sum Arrays

| Field | Value |
|-------|-------|
| Slug | sum-arrays |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/53dc54212259ed3d4f00071c |
| Status | backfilled |
| Reference | languages/python/8kyu/sum-arrays.py |

## Summary

Write a function that takes an array of numbers and returns their sum. Numbers may be negative or floating-point. If the array is empty, return 0.

## Input / Output

- **Input:** An array of numbers (possibly empty).
- **Output:** The numeric sum of all elements.
- **Constraints:** Input is a valid array containing only numbers; may include negatives and decimals.

## Examples

| Input | Output |
|-------|--------|
| `[1, 5.2, 4, 0, -1]` | `9.2` |
| `[-2.398]` | `-2.398` |
| `[]` | `0` |
| `[3, -3]` | `0` |

## Edge Cases

- Empty array → `0`.
- Single element → that element.
- Mix of integers and floats → floating-point sum.

## Approach

- **Algorithm:** Iterate over the array and accumulate each value into a running total.
- **Time:** O(n), where n is array length.
- **Space:** O(1) extra space.

## Behavioral Contract

- Empty input returns `0` (not `null`/`nil`).
- Do not mutate the input array.
- Support negative and fractional values.

## Pseudocode

```text
FUNCTION sum_array(a):
  total = 0
  FOR EACH value IN a:
    total = total + value
  RETURN total
```

## Walkthrough

For `a = [1, 5.2, 4, 0, -1]`:

1. `total = 0 + 1 = 1`.
2. `total = 1 + 5.2 = 6.2`.
3. `total = 6.2 + 4 = 10.2`.
4. `total = 10.2 + 0 = 10.2`.
5. `total = 10.2 + (-1) = 9.2`.
6. Return `9.2`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function sum(numbers)` | `numbers.reduce((a, b) => a + b, 0)` |
| Python | `def sum_array(a)` | Built-in `sum(a)` |
