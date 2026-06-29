# Tortoise racing

| Field | Value |
|-------|-------|
| Slug | tortoise-racing |
| Kyu | 6 |
| Link | https://www.codewars.com/kata/55e2adece53b4cdcb900006c |
| Status | backfilled |
| Reference | languages/python/6kyu/tortoise-racing.py |

## Summary

Two tortoises race: tortoise A moves at `v1` feet/hour and tortoise B at `v2` feet/hour. When B starts, A already leads by `g` feet. Compute how long until B catches A, expressed as whole hours, minutes, and seconds (floor at each decomposition step). If B never catches A (`v1 >= v2`), return the kata's sentinel for "impossible."

## Input / Output

- **Input:** Integers `v1`, `v2`, `g` (speeds in ft/h, gap in feet).
- **Output:** `[hour, minute, second]` of elapsed time with integer components, or impossible sentinel when `v1 >= v2`.
- **Constraints:** Use integer/floor division when converting total seconds to h/m/s.

## Examples

| Input | Output |
|-------|--------|
| `v1=72`, `v2=85`, `g=7` | `[0, 32, 18]` |
| `v1=80`, `v2=91`, `g=70` | `[6, 21, 49]` |
| `v1=100`, `v2=90`, `g=70` | impossible (B slower) |

## Edge Cases

- `v1 >= v2` → B never catches A.
- Catch time computed as `totalSeconds = floor(g * 3600 / (v2 - v1))`.
- Decompose: `h = totalSeconds / 3600`, `m = (totalSeconds % 3600) / 60`, `s = totalSeconds % 60` (integer division throughout).

## Approach

- **Algorithm:** If `v1 >= v2`, return impossible. Else compute closing time in seconds from relative speed, floor, then split into h/m/s.
- **Time:** O(1).
- **Space:** O(1).

## Behavioral Contract

- Speeds and gap are non-negative integers in kata tests; relative speed `(v2 - v1)` is positive when catch is possible.
- Total elapsed seconds uses floor: `floor(g * 3600 / (v2 - v1))`.
- Impossible case: return `null` / `None` in dynamic languages; Go uses `[-1, -1, -1]` per platform skeleton.
- Do not round up partial seconds.

## Pseudocode

```text
FUNCTION race(v1, v2, g):
  IF v1 >= v2:
    RETURN IMPOSSIBLE_SENTINEL
  totalSeconds = FLOOR(g * 3600 / (v2 - v1))
  hours = totalSeconds / 3600
  minutes = (totalSeconds MOD 3600) / 60
  seconds = totalSeconds MOD 60
  RETURN [hours, minutes, seconds]
```

## Walkthrough

For `v1=72`, `v2=85`, `g=7`:

1. `v2 > v1` → catch is possible; relative speed `85 - 72 = 13` ft/h.
2. `totalSeconds = floor(7 * 3600 / 13) = floor(1938.46…) = 1938`.
3. `hours = 1938 / 3600 = 0`, `minutes = (1938 % 3600) / 60 = 32`, `seconds = 1938 % 60 = 18`.
4. Return `[0, 32, 18]`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `func Race(v1, v2, g int) [3]int` | Impossible → `[-1, -1, -1]` |
| Groovy | `static List race(int v1, int v2, int g)` | Impossible → `null` |
| JavaScript | `function race(v1, v2, g)` | Impossible → `null`; explicit `Math.floor` on total seconds |
| Python | `def race(v1, v2, g)` | Impossible → `None`; integer `//` division |
