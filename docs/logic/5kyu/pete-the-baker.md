# Pete, the baker

| Field | Value |
|-------|-------|
| Slug | pete-the-baker |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/525c65e51bf619685c000059 |
| Status | backfilled |
| Reference | languages/python/5kyu/pete-the-baker.py |

## Summary

Given a recipe (ingredient → amount needed per cake) and available ingredient amounts, compute how many whole cakes can be baked. Missing ingredients count as zero available.

## Input / Output

- **Input:** `recipe` map and `available` map (ingredient → quantity).
- **Output:** Non-negative integer count of complete cakes.
- **Constraints:** Only whole cakes; partial amounts do not count.

## Examples

| Input | Output |
|-------|--------|
| `{flour: 500, sugar: 200, eggs: 1}`, `{flour: 1200, sugar: 1200, eggs: 5, milk: 200}` | 2 |
| `{apples: 3}`, `{apples: 6}` | 2 |
| `{flour: 500}`, `{flour: 0}` | 0 |

## Edge Cases

- Ingredient in recipe but absent from `available` → treat as 0.
- Recipe entry with need 0 → skip (does not limit batch size).
- Empty recipe → 0 cakes (no limiting ingredients).
- Extra keys in `available` not in recipe are ignored.

## Approach

- **Algorithm:** For each recipe ingredient with positive need, compute `available[ingredient] // need`; return the minimum of those quotients.
- **Time:** O(r) where r is recipe size
- **Space:** O(1) beyond input maps

## Behavioral Contract

- Integer division (floor) for partial batches.
- `min` over per-ingredient limits; if no positive needs, return 0.
- Missing key in `available` defaults to 0.

## Pseudocode

```text
FUNCTION cakes(recipe, available):
  limits = []

  FOR EACH (ingredient, need) IN recipe:
    IF need == 0:
      CONTINUE
    have = available[ingredient] IF ingredient IN available ELSE 0
    APPEND (have // need) TO limits

  IF limits IS EMPTY:
    RETURN 0

  RETURN MIN(limits)
```

## Walkthrough

Recipe `{flour: 500, sugar: 200, eggs: 1}`; available `{flour: 1200, sugar: 1200, eggs: 5}`:

1. flour: 1200 // 500 = 2
2. sugar: 1200 // 200 = 6
3. eggs: 5 // 1 = 5
4. min(2, 6, 5) → **2**

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `Cakes` | |
| JavaScript | `cakes` | |
| Python | `cakes(recipe, available)` | Min of quotients |
