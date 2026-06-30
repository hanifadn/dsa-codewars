# Array.diff

| Field | Value |
|-------|-------|
| Slug | array-diff |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/523f5d21c841566fde000009 |
| Status | backfilled |
| Reference | languages/javascript/6kyu/array-diff.js |

## Summary

Given two lists, return a new list containing every element of the first list that does not appear in the second list. Preserve the order of survivors from the first list.

## Input / Output

- **Input:** List `a`, list `b`.
- **Output:** List of elements from `a` not present in `b` (by value), in original order.
- **Constraints:** Membership uses equality as defined by the kata tests (typically strict/value equality for numbers).

## Examples

| Input | Output |
|-------|--------|
| `[1, 2]`, `[1]` | `[2]` |
| `[1, 2, 2, 2, 3]`, `[2]` | `[1, 3]` |
| `[1, 2, 3]`, `[4, 5]` | `[1, 2, 3]` |

## Edge Cases

- Empty `a` → empty result.
- Empty `b` → copy/order-preserving view of `a`.
- Duplicates in `a`: each occurrence is removed if its value appears anywhere in `b`.
- All elements removed → empty list.

## Approach

- **Algorithm:** Filter `a`, keeping items where `item` is not contained in `b`.
- **Time:** O(|a| × |b|) with linear search in `b`; can be O(|a| + |b|) with a set.
- **Space:** O(|b|) if using a membership set; O(|a|) for output.

## Behavioral Contract

- Only elements from `a` appear in the result; `b` supplies a removal mask, not output values.
- Order follows `a`, not `b`.
- If a value exists in `b`, every matching value is stripped from `a`.

## Pseudocode

```text
FUNCTION arrayDiff(a, b):
  result = EMPTY LIST
  FOR EACH item IN a:
    IF item NOT IN b:
      APPEND item TO result
  RETURN result
```

## Walkthrough

For `a = [1, 2, 2, 2, 3]`, `b = [2]`:

1. `1` not in `b` → keep.
2. Each `2` is in `b` → skip all three.
3. `3` not in `b` → keep.
4. Return `[1, 3]`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function arrayDiff(a, b)` | `filter` with `!b.includes(item)` |
