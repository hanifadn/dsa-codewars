# Moving Zeros to the End

| Field | Value |
|-------|-------|
| Slug | moving-zeros-to-the-end |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/52597aa56021e91c93000cb0 |
| Status | backfilled |
| Reference | languages/javascript/5kyu/moving-zeros-to-the-end.js |

## Summary

Reorder an array so every element strictly equal to numeric zero appears at the end, while all other elements keep their relative order.

## Input / Output

- **Input:** An array of mixed types (numbers, booleans, strings, etc.).
- **Output:** A new array with the same elements reordered: non-zeros first (stable order), then all zeros.
- **Constraints:** Only the number `0` is treated as zero; `false`, `"0"`, and `-0` are not moved.

## Examples

| Input | Output |
|-------|--------|
| `[1, 0, 1, 3, 0]` | `[1, 1, 3, 0, 0]` |
| `[false, 1, 0, 1, 2, 0, 1, 3, "a"]` | `[false, 1, 1, 2, 1, 3, "a", 0, 0]` |
| `[0, 0, 0]` | `[0, 0, 0]` |
| `[]` | `[]` |

## Edge Cases

- No zeros → return a copy with identical order.
- All zeros → unchanged order of zeros.
- Strict equality: only `0` moves, not other falsy values.

## Approach

- **Algorithm:** Partition into non-zero elements (preserving order) and zero elements (preserving order); concatenate.
- **Time:** O(n)
- **Space:** O(n) for the result array

## Behavioral Contract

- Use strict numeric zero test (`=== 0` / exact equality to integer 0).
- Stable sort behavior for both partitions.
- Return a new array; do not require in-place mutation (either is acceptable on Codewars if tests allow).

## Pseudocode

```text
FUNCTION moveZeros(arr):
  nonZeros = []
  zeros = []

  FOR EACH item IN arr:
    IF item == 0:
      APPEND item TO zeros
    ELSE:
      APPEND item TO nonZeros

  RETURN CONCATENATE(nonZeros, zeros)
```

## Walkthrough

For `[false, 1, 0, 1, 2, 0, 1, 3, "a"]`:

1. `false` → nonZeros; `1` → nonZeros; `0` → zeros; `1` → nonZeros; `2` → nonZeros; `0` → zeros; `1`, `3`, `"a"` → nonZeros.
2. Concatenate → `[false, 1, 1, 2, 1, 3, "a", 0, 0]`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `moveZeros(arr)` | Stable partition |
