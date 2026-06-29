# Find the smallest integer in the array

| Field | Value |
|-------|-------|
| Slug | find-the-smallest-integer-in-the-array |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/55a2d7ebe362935a210000b2 |
| Status | backfilled |
| Reference | languages/groovy/8kyu/find-the-smallest-integer-in-the-array.groovy |

## Summary

Given an array of integers, find and return the smallest integer. The array is guaranteed to contain at least one element.

## Input / Output

- **Input:** A non-empty array/list of integers.
- **Output:** The smallest integer in the array.
- **Constraints:** Array will not be empty; negative values are valid.

## Examples

| Input | Output |
|-------|--------|
| `[34, 15, 88, 2]` | `2` |
| `[34, -345, -1, 100]` | `-345` |
| `[5]` | `5` |
| `[0, 1, -1]` | `-1` |

## Edge Cases

- Single-element array → return that element.
- All negative values → return the least negative (closest to zero) or most negative depending on values; e.g. `[-5, -2, -9]` → `-9`.
- Duplicate minimum values → return the minimum value (duplicates do not matter).

## Approach

- **Algorithm:** Scan the array for the minimum value, or use a built-in min operation.
- **Time:** O(n), where n is array length.
- **Space:** O(1) extra space.

## Behavioral Contract

- Input array is never empty.
- Do not mutate the input array.
- Return the numeric minimum, not its index.

## Pseudocode

```text
FUNCTION findSmallestInt(arr):
  smallest = arr[0]
  FOR EACH value IN arr:
    IF value < smallest:
      smallest = value
  RETURN smallest
```

## Walkthrough

For `arr = [34, -345, -1, 100]`:

1. Initialize `smallest = 34`.
2. Compare `-345 < 34` → `smallest = -345`.
3. Compare `-1 < -345` → no change.
4. Compare `100 < -345` → no change.
5. Return `-345`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static int findSmallestInt(ArrayList arr)` | `arr.min()` |
