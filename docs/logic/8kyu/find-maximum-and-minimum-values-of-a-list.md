# Find Maximum and Minimum Values of a List

| Field | Value |
|-------|-------|
| Slug | find-maximum-and-minimum-values-of-a-list |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/577a98a6ae28071780000989 |
| Status | backfilled |
| Reference | languages/python/8kyu/find-maximum-and-minimum-values-of-a-list.py |

## Summary

Implement two separate functions that each receive a list of integers and return a single number: one returns the smallest value, the other returns the largest. The input list is never empty.

## Input / Output

- **Input:** A non-empty list/array of integers.
- **Output:** Two functions — `minimum`/`min` returns the smallest element; `maximum`/`max` returns the largest element.
- **Constraints:** Input is guaranteed non-empty; each function returns one integer.

## Examples

| Input | minimum | maximum |
|-------|---------|---------|
| `[4, 6, 2, 1, 9, 63, -134, 566]` | `-134` | `566` |
| `[-52, 56, 30, 29, -54, 0, -110]` | `-110` | `56` |
| `[42, 54, 65, 87, 0]` | `0` | `87` |
| `[5]` | `5` | `5` |

## Edge Cases

- Single-element list → that element is both min and max.
- All equal values → min equals max.
- List contains negative, zero, and positive values.

## Approach

- **Algorithm:** Scan the list (or use built-in min/max) to find the smallest and largest values independently.
- **Time:** O(n) per function, where n is list length.
- **Space:** O(1) extra space.

## Behavioral Contract

- Input list is never empty; no special empty-input handling required.
- Do not mutate the input list.
- `minimum` and `maximum` are separate entry points returning one number each.

## Pseudocode

```text
FUNCTION minimum(arr):
  smallest = arr[0]
  FOR EACH value IN arr:
    IF value < smallest:
      smallest = value
  RETURN smallest

FUNCTION maximum(arr):
  largest = arr[0]
  FOR EACH value IN arr:
    IF value > largest:
      largest = value
  RETURN largest
```

## Walkthrough

For `arr = [4, 6, 2, 1, 9, 63, -134, 566]`:

1. `minimum`: scan finds `-134` as the smallest → return `-134`.
2. `maximum`: scan finds `566` as the largest → return `566`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function min(list)` / `function max(list)` | `Math.min(...list)` / `Math.max(...list)` |
| Python | `def minimum(arr)` / `def maximum(arr)` | Built-in `min(arr)` / `max(arr)` |
