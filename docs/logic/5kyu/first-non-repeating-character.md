# First Non-Repeating Character

| Field | Value |
|-------|-------|
| Slug | first-non-repeating-character |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/52bc74d4ac05d0945d00054e |
| Status | backfilled |
| Reference | languages/javascript/5kyu/first-non-repeating-character.js |

## Summary

Return the first character in a string that appears exactly once. Letter case is ignored when counting repeats, but the returned character must preserve the casing from the original string. Return an empty string when every character repeats.

## Input / Output

- **Input:** A string `s` (may include Unicode code points).
- **Output:** A one-character string from `s`, or `""` if none qualifies.
- **Constraints:** Case-insensitive frequency; case-sensitive return value.

## Examples

| Input | Output |
|-------|--------|
| `"stress"` | `"t"` |
| `"sTreSS"` | `"T"` |
| `"@#@@*"` | `"#"` |
| `"かか何"` | `"何"` |
| `"🐐🦊🐐"` | `"🦊"` |
| `"aabb"` | `""` |

## Edge Cases

- Empty string → `""`.
- Single character → that character.
- Upper and lower of the same letter count as one symbol for frequency.
- Emoji and non-Latin scripts use full code-point equality after lowercasing rules of the language.

## Approach

- **Algorithm:** Two passes — build case-insensitive frequency map, then scan left-to-right for the first index whose lowercased form has count 1; return `s[i]` at that index.
- **Time:** O(n)
- **Space:** O(k) where k is the number of distinct characters

## Behavioral Contract

- Comparison uses case folding (e.g. lowercase) for counting only.
- Return value is the exact substring unit at the matching index (preserves original case).
- All-repeating input → `""` (not null).

## Pseudocode

```text
FUNCTION firstNonRepeatingLetter(s):
  lower = CASE_FOLD(s)  // per-language lowercase
  freq = EMPTY MAP

  FOR EACH char IN lower:
    freq[char] = freq[char] + 1

  FOR i FROM 0 TO LENGTH(s) - 1:
    IF freq[lower[i]] == 1:
      RETURN s[i]

  RETURN ""
```

## Walkthrough

For `"sTreSS"`:

1. Lowercase scan: `s→2, t→1, r→1, e→1` wait - `s` appears at 0 and 4, `S` at 4 → `s` count 2. `t→1`, `r→1`, `e→1`.
2. Index 0: `s` count 2 — skip.
3. Index 1: `t` count 1 — return `s[1]` → **`"T"`**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `firstNonRepeatingLetter(s)` | Two-pass frequency |
