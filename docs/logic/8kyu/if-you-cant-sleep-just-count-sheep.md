# If you can't sleep, just count sheep!!

| Field | Value |
|-------|-------|
| Slug | if-you-cant-sleep-just-count-sheep |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/5b077ebdaf15be5c7f000077 |
| Status | backfilled |
| Reference | languages/python/8kyu/if-you-cant-sleep-just-count-sheep.py |

## Summary

Given a non-negative integer `n`, return a single string that counts sheep from 1 to `n` in the pattern `"1 sheep...2 sheep...3 sheep..."`. For `n = 0`, return an empty string.

## Input / Output

- **Input:** A non-negative integer `n`.
- **Output:** A concatenated string of counted sheep, or `""` when `n` is 0.
- **Constraints:** Input is always valid (non-negative); no negative integers.

## Examples

| Input | Output |
|-------|--------|
| `0` | `""` |
| `1` | `"1 sheep..."` |
| `2` | `"1 sheep...2 sheep..."` |
| `3` | `"1 sheep...2 sheep...3 sheep..."` |

## Edge Cases

- `n = 0` → empty string (no sheep counted).
- `n = 1` → single phrase with no leading/trailing extra spaces beyond the pattern.

## Approach

- **Algorithm:** Loop from 1 to `n` inclusive, append `"{i} sheep..."` to a result string for each `i`.
- **Time:** O(n) in the length of the output string.
- **Space:** O(n) for the result string.

## Behavioral Contract

- Count starts at 1, not 0.
- Each segment ends with `" sheep..."` (three dots).
- Segments are concatenated with no separator between them.
- `n = 0` yields `""`.

## Pseudocode

```text
FUNCTION count_sheep(n):
  result = ""
  FOR i FROM 1 TO n INCLUSIVE:
    result = result + STRING(i) + " sheep..."
  RETURN result
```

## Walkthrough

For `n = 3`:

1. `i = 1` → `result = "1 sheep..."`.
2. `i = 2` → `result = "1 sheep...2 sheep..."`.
3. `i = 3` → `result = "1 sheep...2 sheep...3 sheep..."`.
4. Return the final string.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `func countSheep(num int) string` | `strings.Builder`, loop 1..num |
| JavaScript | `function countSheep(n)` | Loop and string concatenation |
| Python | `def count_sheep(n)` | `''.join(f"{i} sheep..." for i in range(1, n + 1))` |
