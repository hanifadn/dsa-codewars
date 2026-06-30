# Break CamelCase

| Field | Value |
|-------|-------|
| Slug | break-camelcase |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/5208f99aee097e6552000148 |
| Status | backfilled |
| Reference | languages/javascript/6kyu/break-camelcase.js |

## Summary

Split a camelCase string into words separated by spaces. Insert a space immediately before each uppercase letter; leave all other characters unchanged.

## Input / Output

- **Input:** A string (possibly empty).
- **Output:** The same characters with a single space inserted before each uppercase letter.
- **Constraints:** Only ASCII uppercase `A`–`Z` trigger word breaks; no trimming of the original text.

## Examples

| Input | Output |
|-------|--------|
| `"camelCasing"` | `"camel Casing"` |
| `"identifier"` | `"identifier"` |
| `""` | `""` |
| `"CamelCaseWord"` | `" Camel Case Word"` |

## Edge Cases

- Empty string → empty string.
- No uppercase letters → unchanged input.
- Leading uppercase adds a leading space (e.g. `"Camel"` → `" Camel"` per the replacement rule).

## Approach

- **Algorithm:** Replace every uppercase letter with `" " + letter` using a global pattern.
- **Time:** O(n) over string length.
- **Space:** O(n) for the new string.

## Behavioral Contract

- Preserve original letter casing in the output.
- Only uppercase boundaries receive a preceding space.
- Do not collapse or trim internal whitespace beyond inserted breaks.

## Pseudocode

```text
FUNCTION solution(string):
  RETURN REPLACE EACH UPPERCASE CHARACTER c IN string WITH (" " + c)
```

## Walkthrough

For `"camelCasing"`:

1. Uppercase at index 5: `'C'`.
2. Replace → `"camel" + " " + "Casing"`.
3. Return `"camel Casing"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `function solution(string)` | `replace(/([A-Z])/g, ' $1')` |
