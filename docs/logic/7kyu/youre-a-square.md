# You're a square!

| Field | Value |
|-------|-------|
| Slug | youre-a-square |
| Kyu | 7 |
| Link | https://www.codewars.com/kata/54c27a33fb7da0db0100040e |
| Status | backfilled |
| Reference | languages/groovy/7kyu/youre-a-square.groovy |

## Summary

Determine whether a given integer is a perfect square: an integer equal to some integer multiplied by itself.

## Input / Output

- **Input:** An integer `n`.
- **Output:** Boolean — `true` if `n` is a perfect square, otherwise `false`.
- **Constraints:** Negative integers are not perfect squares.

## Examples

| Input | Output |
|-------|--------|
| `-1` | `false` |
| `0` | `true` |
| `3` | `false` |
| `4` | `true` |
| `25` | `true` |
| `26` | `false` |

## Edge Cases

- `0` → `true` (`0 * 0`).
- Negative numbers → `false` immediately.
- Large perfect squares within integer range.

## Approach

- **Algorithm:** Reject negatives. Let `r = floor(sqrt(n))`. Return whether `r * r == n`.
- **Time:** O(1) with floating-point or integer square root.
- **Space:** O(1).

## Behavioral Contract

- Perfect square means ∃ integer k such that k² = n.
- Negative inputs always yield `false`.
- Use integer arithmetic for the final equality check to avoid float rounding on large values when possible.

## Pseudocode

```text
FUNCTION isSquare(n):
  IF n < 0:
    RETURN false
  r = FLOOR(SQRT(n))
  RETURN r * r == n
```

## Walkthrough

For `n = 25`:

1. `n >= 0` → continue.
2. `r = floor(sqrt(25)) = 5`.
3. `5 * 5 == 25` → return `true`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static boolean isSquare(int n)` | Early exit for negatives; compare `floorSqrt * floorSqrt` |
