# Get the Middle Character

| Field | Value |
|-------|-------|
| Slug | get-the-middle-character |
| Kyu | 7 |
| Link | https://www.codewars.com/kata/56747fd5cb988479af000028 |
| Status | backfilled |
| Reference | languages/javascript/7kyu/get-the-middle-character.js |

## Summary

Return the middle portion of a non-empty string. For odd length, return the single middle character. For even length, return the two middle characters in order.

## Input / Output

- **Input:** A non-empty string `s`.
- **Output:** A string of length 1 (odd input) or 2 (even input).
- **Constraints:** Input is never empty; preserve original character casing.

## Examples

| Input | Output |
|-------|--------|
| `"test"` | `"es"` |
| `"testing"` | `"t"` |
| `"middle"` | `"dd"` |
| `"A"` | `"A"` |

## Edge Cases

- Length 1 → return the whole string.
- Even length → two characters centered around the middle index.
- Odd length → one character at index `floor(len / 2)`.

## Approach

- **Algorithm:** Compute `mid = floor(len / 2)`. If length is even, slice `[mid - 1, mid + 1)`; otherwise take the character at `mid`.
- **Time:** O(1) for indexing/slicing (excluding output copy).
- **Space:** O(1) or O(2) for the result.

## Behavioral Contract

- Input is guaranteed non-empty.
- Even-length results contain exactly two characters from the original string.
- Do not trim, lower-case, or otherwise transform characters.

## Pseudocode

```text
FUNCTION getMiddle(s):
  len = LENGTH(s)
  mid = FLOOR(len / 2)
  IF len MOD 2 == 0:
    RETURN SUBSTRING(s, mid - 1, mid + 1)
  ELSE:
    RETURN CHARACTER AT s[mid]
```

## Walkthrough

For `s = "test"` (length 4):

1. `mid = 2`.
2. Length is even → substring from index 1 through 2 → `"es"`.
3. Return `"es"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function getMiddle(s)` | Slice or single `charAt` by parity |
