# The Hashtag Generator

| Field | Value |
|-------|-------|
| Slug | the-hashtag-generator |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/52449b062fb80683ec000024 |
| Status | backfilled |
| Reference | languages/python/5kyu/the-hashtag-generator.py |

## Summary

Convert a string into a hashtag: `#` followed by words title-cased and concatenated without spaces. Return `False` when the input is empty or whitespace-only, or when the result exceeds 140 characters.

## Input / Output

- **Input:** String `s`.
- **Output:** Hashtag string or boolean `False` on failure.
- **Constraints:** Max length 140 including `#`; words split on whitespace.

## Examples

| Input | Output |
|-------|--------|
| `"Hello World"` | `"#HelloWorld"` |
| `"hello world"` | `"#HelloWorld"` |
| `"Codewars is nice"` | `"#CodewarsIsNice"` |
| `""` | `False` |
| `"   "` | `False` |
| Very long input (>140 after formatting) | `False` |

## Edge Cases

- Multiple internal spaces collapse via split-on-whitespace.
- Each word: first character uppercased, remainder lowercased.
- Single-word input works normally.
- Length check is on the final tag string.

## Approach

- **Algorithm:** Split into words; if none, return `False`. Build `#` + join of title-cased words; return `False` if `len > 140`, else tag.
- **Time:** O(n)
- **Space:** O(n)

## Behavioral Contract

- Failure returns `False` (not `null`, not empty string).
- Title case per word, not per sentence.
- Leading/trailing whitespace-only → `False`.

## Pseudocode

```text
FUNCTION generateHashtag(s):
  words = SPLIT s ON WHITESPACE (discard empty tokens)
  IF words IS EMPTY:
    RETURN False

  tag = "#"
  FOR EACH word IN words:
    tag = tag + UPPER(word[0]) + LOWER(word[1:])

  IF LENGTH(tag) > 140:
    RETURN False

  RETURN tag
```

## Walkthrough

For `"codewars is nice"`:

1. words = `["codewars", "is", "nice"]`
2. tag = `#` + `Codewars` + `Is` + `Nice` = `#CodewarsIsNice`
3. Length ≤ 140 → return **`#CodewarsIsNice`**

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `generateHashtag` | |
| JavaScript | `generateHashtag` | |
| Python | `generate_hashtag(s)` | Returns False on failure |
