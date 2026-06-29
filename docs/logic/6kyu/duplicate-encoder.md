# Duplicate Encoder

| Field | Value |
|-------|-------|
| Slug | duplicate-encoder |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/54b42f9314d9229fd6000d9c |
| Status | backfilled |
| Reference | languages/javascript/6kyu/duplicate-encoder.js |

## Summary

Transform a string into a parenthesis string of the same length: emit `'('` for characters that appear exactly once in the original (case insensitive) and `')'` for characters that appear more than once. Non-letters keep their identity for counting but casing is ignored when tallying letters.

## Input / Output

- **Input:** A string `word`.
- **Output:** A string of `'('` and `')'` with the same length as `word`.
- **Constraints:** Duplicate detection is case insensitive; output length equals input length.

## Examples

| Input | Output |
|-------|--------|
| `"din"` | `"((("` |
| `"recede"` | `"()()()"` |
| `"Success"` | `")())())"` |
| `"(( @"` | `"))(("` |

## Edge Cases

- All unique characters → all `'('`.
- All characters duplicated (frequency ≥ 2) → all `')'`.
- Mixed case maps to one bucket (`S` and `s` share frequency).
- Spaces and punctuation participate in frequency and output position.

## Approach

- **Algorithm:** Lowercase for counting, build frequency map, map each lowercased character to `'('` if count == 1 else `')'`, preserve traversal order of original lowercased chars.
- **Time:** O(n).
- **Space:** O(n) for frequency map and output.

## Behavioral Contract

- Case insensitive frequency; iterate using case-folded characters for mapping decisions.
- Position i in output corresponds to position i in input.
- Character with frequency 1 → `'('`; frequency ≥ 2 → `')'`.

## Pseudocode

```text
FUNCTION duplicateEncode(word):
  lower = LOWERCASE(word)
  frequencies = EMPTY MAP
  FOR EACH char IN lower:
    frequencies[char] = frequencies[char] + 1
  result = EMPTY STRING
  FOR EACH char IN lower:
    IF frequencies[char] == 1:
      APPEND "(" TO result
    ELSE:
      APPEND ")" TO result
  RETURN result
```

## Walkthrough

For `"Success"` → lower `"success"`:

1. Frequencies: `s→3`, `u→1`, `c→1`, `e→1`.
2. Map each char: `s→')'`, `u→'('`, `c→'('`, `c→'('`, `e→'('`, `s→')'`, `s→')'`.
3. Return `")())())"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function duplicateEncode(word)` | Frequency pass, then map lowercased chars |
