# Create Phone Number

| Field | Value |
|-------|-------|
| Slug | create-phone-number |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/525f50e3b73515a6db000b83 |
| Status | backfilled |
| Reference | languages/javascript/6kyu/create-phone-number.js |

## Summary

Format an array of exactly ten single-digit integers (0–9) as a US-style phone number string: `(XXX) XXX-XXXX`, including the space after the closing parenthesis.

## Input / Output

- **Input:** Array of 10 integers, each in `0..9`.
- **Output:** String `"(XXX) XXX-XXXX"` where each `X` is the corresponding digit.
- **Constraints:** Input length is always 10; digits are concatenated in order without separators before formatting.

## Examples

| Input | Output |
|-------|--------|
| `[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]` | `"(123) 456-7890"` |

## Edge Cases

- Leading zero in the number (e.g. last digit `0`) must appear in output.
- All digits identical still follows the same mask.
- Formatting is fixed; no country code or alternate separators.

## Approach

- **Algorithm:** Join digits into a 10-character string, then apply pattern `(\\d{3})(\\d{3})(\\d{4})` → `($1) $2-$3`.
- **Time:** O(1) — fixed 10 digits.
- **Space:** O(1) for output string.

## Behavioral Contract

- Exactly ten digits; no extra punctuation in input.
- Output must match `(NNN) NNN-NNNN` literally, including parentheses, space, and hyphen positions.
- Digits are taken in array order left to right.

## Pseudocode

```text
FUNCTION createPhoneNumber(numbers):
  digits = JOIN numbers AS STRINGS WITH NO SEPARATOR
  area = SUBSTRING(digits, 0, 3)
  prefix = SUBSTRING(digits, 3, 6)
  line = SUBSTRING(digits, 6, 10)
  RETURN "(" + area + ") " + prefix + "-" + line
```

## Walkthrough

For `[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]`:

1. Join → `"1234567890"`.
2. Split → area `"123"`, prefix `"456"`, line `"7890"`.
3. Format → `"(123) 456-7890"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function createPhoneNumber(numbers)` | Join then regex replace with capture groups |
