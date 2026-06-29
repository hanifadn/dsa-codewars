# 4 By 4 Skyscrapers

| Field | Value |
|-------|-------|
| Slug | 4-by-4-skyscrapers |
| Kyu | 4 |
| Link | https://www.codewars.com/kata/5671d975d81d6c1c87000022 |
| Status | backfilled |
| Reference | languages/python/4kyu/4-by-4-skyscrapers.py |

## Summary

Solve a 4×4 skyscraper puzzle. Place heights 1–4 in each cell so every row and column is a permutation of 1–4. Sixteen edge clues (clockwise around the grid; `0` means unknown) state how many buildings are visible from that direction—taller buildings hide shorter ones behind them.

## Input / Output

- **Input:** `clues` — 16 integers in clockwise order: top (left→right), right (top→bottom), bottom (right→left), left (bottom→top).
- **Output:** 4×4 grid as nested tuples/arrays of ints 1–4.
- **Constraints:** Exactly one valid solution for test inputs.

## Examples

| Clues (abbrev.) | Result |
|-----------------|--------|
| Standard puzzle clues | Unique 4×4 Latin square matching all non-zero edge views |

Clue index layout (clockwise from top-left of top row):

```text
        clues[0..3]   (top)
clues[15..12]              clues[4..7]   (right)
        clues[11..8]  (bottom, reversed col order)
```

## Edge Cases

- Clue `0` imposes no constraint on that side.
- Row/column must each contain 1, 2, 3, 4 exactly once.
- Visibility count from a line is the number of strict left-to-right (or top-to-bottom) maxima.

## Approach

- **Algorithm:** Pre-filter each row's permutations by left/right clues. DFS row-by-row; prune when a column would duplicate a height above or when final column top/bottom clues fail.
- **Time:** O(24^4) worst case, heavily pruned in practice
- **Space:** O(16) grid + row option lists

## Behavioral Contract

- `countVisible(heights)`: scan line, increment when height exceeds all previous max.
- Clue at index `15 - row` is left of row `row`; `4 + row` is right of row `row`.
- Top clue for column `c` is `clues[c]`; bottom for column `c` is `clues[8 + (3 - c)]`.
- Return type is tuple of row tuples.

## Pseudocode

```text
FUNCTION countVisible(heights):
  tallest = 0
  seen = 0
  FOR h IN heights:
    IF h > tallest:
      tallest = h
      seen += 1
  RETURN seen

FUNCTION rowOptions(rowIndex, clues):
  leftClue = clues[15 - rowIndex]
  rightClue = clues[4 + rowIndex]
  RETURN all permutations of (1,2,3,4) where
    (leftClue == 0 OR countVisible(row) == leftClue) AND
    (rightClue == 0 OR countVisible(REVERSE(row)) == rightClue)

FUNCTION columnsValid(grid, clues):
  FOR col FROM 0 TO 3:
    column = [grid[r][col] for r in 0..3]
    topClue = clues[col]
    bottomClue = clues[8 + (3 - col)]
    IF topClue != 0 AND countVisible(column) != topClue: RETURN False
    IF bottomClue != 0 AND countVisible(REVERSE(column)) != bottomClue: RETURN False
  RETURN True

FUNCTION columnClash(grid, row, choice):
  FOR col IN 0..3:
    FOR above IN 0..row-1:
      IF grid[above][col] == choice[col]: RETURN True
  RETURN False

FUNCTION dfs(row, grid, rowOptionsByRow, clues):
  IF row == 4:
    RETURN COPY(grid) IF columnsValid(grid, clues) ELSE None
  FOR choice IN rowOptionsByRow[row]:
    IF columnClash(grid, row, choice): CONTINUE
    ASSIGN choice TO grid[row]
    solved = dfs(row + 1, grid, rowOptionsByRow, clues)
    IF solved != None: RETURN solved
  RETURN None

FUNCTION solvePuzzle(clues):
  rowOptionsByRow = [rowOptions(i, clues) for i in 0..3]
  grid = 4x4 zeros
  RETURN dfs(0, grid, rowOptionsByRow, clues) AS tuple of row tuples
```

## Walkthrough

Row 0 options filtered by top clue `clues[15]` and right clue `clues[4]`. Pick a valid row, ensure no column duplicate with rows above, recurse. After placing row 3, verify all column top/bottom clues; first complete grid that passes is the answer.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `SolvePuzzle` | |
| JavaScript | `solvePuzzle` | |
| Python | `solve_puzzle(clues)` | Row DFS + clue pruning |
