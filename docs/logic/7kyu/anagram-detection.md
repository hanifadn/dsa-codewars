# Anagram Detection

| Field | Value |
|-------|-------|
| Slug | anagram-detection |
| Kyu | 7 |
| Link | https://www.codewars.com/kata/529eef7a9194e0cbc1000255 |
| Status | backfilled |
| Reference | languages/groovy/7kyu/anagram-detection.groovy |

## Summary

Given two strings, decide whether one is an anagram of the other. An anagram uses exactly the same multiset of letters rearranged into a different order. Letter comparison is case insensitive.

## Input / Output

- **Input:** Two strings (`test`, `original`).
- **Output:** Boolean — `true` if the strings are anagrams, otherwise `false`.
- **Constraints:** Comparison ignores letter case; non-letter characters are compared as-is if present in the input.

## Examples

| Input | Output |
|-------|--------|
| `"foefet"`, `"toffee"` | `true` |
| `"Buckethead"`, `"DeathCubeK"` | `true` |
| `"hello"`, `"world"` | `false` |

## Edge Cases

- Identical strings (including same casing) → `true`.
- Same letters with different casing → `true`.
- Different lengths → `false`.
- Empty strings → `true` (both have zero letters).

## Approach

- **Algorithm:** Normalize both strings to lowercase, sort their characters, and compare the sorted sequences.
- **Time:** O(n log n) per string for sorting, where n is string length.
- **Space:** O(n) for the sorted character lists.

## Behavioral Contract

- Case folding applies before comparison; `'A'` and `'a'` are the same letter.
- Anagram means equal character counts, not merely equal length.
- Do not mutate caller-owned input strings unless the language API requires it.

## Pseudocode

```text
FUNCTION isAnagram(test, original):
  normalizedTest = LOWERCASE(test) AS LIST OF CHARACTERS
  normalizedOriginal = LOWERCASE(original) AS LIST OF CHARACTERS
  SORT normalizedTest
  SORT normalizedOriginal
  RETURN JOIN(normalizedTest) == JOIN(normalizedOriginal)
```

## Walkthrough

For `"foefet"` and `"toffee"`:

1. Lowercase both → same multiset `{f, o, e, e, t, f}`.
2. Sort each → `"eeffot"` for both.
3. Sequences match → return `true`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static boolean isAnagram(String test, String original)` | Sort lowercase character lists and compare |
