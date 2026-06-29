# Convert string to camel case

| Field | Value |
|-------|-------|
| Slug | convert-string-to-camelcase |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/517abf86da9663f1d2000003 |
| Status | backfilled |
| Reference | languages/python/6kyu/convert-string-to-camelcase.py |

## Summary

Convert a string of words separated by hyphens or underscores into camelCase. The first word keeps its original capitalization; every following word is title-cased and concatenated without separators.

## Input / Output

- **Input:** A string using `-` and/or `_` as word delimiters.
- **Output:** A single camelCase/PascalCase string with no delimiters.
- **Constraints:** Delimiters are only `-` and `_`; letters may be mixed case in the input.

## Examples

| Input | Output |
|-------|--------|
| `"the-stealth-warrior"` | `"theStealthWarrior"` |
| `"The_Stealth_Warrior"` | `"TheStealthWarrior"` |
| `"The_Stealth-Warrior"` | `"TheStealthWarrior"` |

## Edge Cases

- Single word with no delimiters → unchanged.
- Empty string → empty string.
- First word capitalization is preserved exactly (not forced lower/upper).
- Later words: first character uppercased, remaining characters lowercased (`capitalize` semantics).

## Approach

- **Algorithm:** Split on `[-_]`, emit `words[0]` verbatim, then append each subsequent word with first letter upper and rest lower.
- **Time:** O(n) over input length.
- **Space:** O(n) for split words and output.

## Behavioral Contract

- Only `-` and `_` are delimiters; they are removed from output.
- First segment casing mirrors input (supports both camelCase and PascalCase starts).
- Segments after the first always use title case per word (`Stealth`, not `STEALTH`).

## Pseudocode

```text
FUNCTION toCamelCase(text):
  words = SPLIT text ON REGEX "[-_]"
  IF words IS EMPTY:
    RETURN ""
  result = words[0]
  FOR EACH word IN words[1..]:
    result = result + CAPITALIZE(word)
  RETURN result

FUNCTION CAPITALIZE(word):
  IF word IS EMPTY:
    RETURN ""
  RETURN UPPER(word[0]) + LOWER(word[1..])
```

## Walkthrough

For `"the-stealth-warrior"`:

1. Split → `["the", "stealth", "warrior"]`.
2. Start with `"the"`.
3. Append `"Stealth"`, then `"Warrior"`.
4. Return `"theStealthWarrior"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Python | `def to_camel_case(text)` | `re.split('[-_]', text)`; first word raw, rest `.capitalize()` |
