# Counting Duplicates

| Field | Value |
|-------|-------|
| Slug | counting-duplicates |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1 |
| Status | backfilled |
| Reference | languages/groovy/6kyu/counting-duplicates.groovy |

## Summary

Count how many distinct alphanumeric characters appear more than once in a string, comparing letters case insensitively and treating digits as themselves.

## Input / Output

- **Input:** A string containing only letters and digits.
- **Output:** Integer count of distinct characters (case-folded) whose frequency is greater than 1.
- **Constraints:** Input charset is letters + digits only.

## Examples

| Input | Output |
|-------|--------|
| `"abcde"` | `0` |
| `"aabbcde"` | `2` (`a`, `b`) |
| `"aabBcde"` | `2` |
| `"indivisibility"` | `1` (`i`) |
| `"Indivisibilities"` | `2` (`i`, `s`) |
| `"aA11"` | `2` (`a`, `1`) |
| `"ABBA"` | `2` (`A`, `B`) |

## Edge Cases

- No repeated characters → `0`.
- Case variants of the same letter aggregate (`a` + `A` → one bucket).
- A character repeated exactly twice counts once toward the answer (count distinct duplicated chars, not excess copies).

## Approach

- **Algorithm:** Lowercase the string, tally each character, count how many tally values exceed 1.
- **Time:** O(n) for n = string length.
- **Space:** O(k) for k distinct characters.

## Behavioral Contract

- Case insensitive for letters; `'A'` and `'a'` share one frequency bucket.
- Digits are caseless and counted normally.
- Return the number of characters with frequency > 1, not total duplicate occurrences.

## Pseudocode

```text
FUNCTION duplicateCount(text):
  normalized = LOWERCASE(text)
  frequencies = EMPTY MAP FROM CHARACTER TO COUNT
  FOR EACH char IN normalized:
    frequencies[char] = frequencies[char] + 1
  count = 0
  FOR EACH freq IN VALUES(frequencies):
    IF freq > 1:
      count = count + 1
  RETURN count
```

## Walkthrough

For `"aabBcde"`:

1. Lowercase → `"aabbcde"`.
2. Frequencies: `a→2`, `b→2`, others → 1.
3. Two characters (`a`, `b`) have frequency > 1 → return `2`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static Integer duplicateCount(String text)` | `countBy` on lowercased chars; count values > 1 |
