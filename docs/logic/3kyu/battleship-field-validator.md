# Battleship field validator

| Field | Value |
|-------|-------|
| Slug | battleship-field-validator |
| Kyu | 3 |
| Link | https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7 |
| Status | backfilled |
| Reference | languages/python/3kyu/battleship-field-validator.py |

## Summary

Validate a 10×10 Battleship field. Cells are `0` (water) or `1` (ship). The fleet must be exactly one ship of length 4, two of length 3, three of length 2, and four of length 1 (20 ship cells total). Each ship is a straight horizontal or vertical segment. Ships may touch orthogonally only within the same ship—never diagonally or at corners between different ships.

## Input / Output

- **Input:** 10×10 grid of 0/1 integers.
- **Output:** Boolean — `true` if valid deployment.
- **Constraints:** Fixed fleet composition; no diagonal adjacency between distinct ships.

## Examples

| Input | Output |
|-------|--------|
| Valid standard fleet layout | `true` |
| Two ship cells touching diagonally | `false` |
| Wrong ship count or length histogram | `false` |
| L-shaped or disconnected ship component | `false` |

## Edge Cases

- Non-10×10 or ragged rows → invalid.
- Total ship cells ≠ 20 → invalid.
- Single-cell ships (length 1) are valid if count is 4.
- Orthogonal chain must fill its bounding box (no gaps in a straight line).

## Approach

- **Algorithm:** (1) shape and cell count checks; (2) scan for diagonal adjacency between occupied cells; (3) flood-fill orthogonal components, verify each is a solid straight segment, tally lengths against `{4:1, 3:2, 2:3, 1:4}`.
- **Time:** O(100)
- **Space:** O(100) visited grid

## Behavioral Contract

- Diagonal touch: any `1` with a `1` at `(row-1, col±1)` invalidates the field.
- Component is valid iff all cells share one row OR one column AND bounding-box area equals component size.
- Histogram must match exactly; extra lengths (e.g. 5) fail.

## Pseudocode

```text
EXPECTED = {4: 1, 3: 2, 2: 3, 1: 4}
SHIP_CELLS = 20

FUNCTION validateBattlefield(field):
  IF NOT 10x10 grid: RETURN False
  IF countOnes(field) != SHIP_CELLS: RETURN False
  IF hasDiagonalShipContact(field): RETURN False

  histogram = {1:0, 2:0, 3:0, 4:0}
  visited = 10x10 False

  FOR each cell (r,c) with field[r][c]==1 and not visited:
    cells = floodFillOrthogonal(field, visited, r, c)
    len = LENGTH(cells)
    IF len NOT IN EXPECTED: RETURN False
    IF NOT isStraightSegment(cells): RETURN False
    histogram[len] += 1

  RETURN histogram == EXPECTED

FUNCTION hasDiagonalShipContact(field):
  FOR r FROM 1 TO 9:
    FOR c FROM 0 TO 9:
      IF field[r][c]==0: CONTINUE
      IF c>0 AND field[r-1][c-1]==1: RETURN True
      IF c<9 AND field[r-1][c+1]==1: RETURN True
  RETURN False

FUNCTION isStraightSegment(cells):
  rows = unique row indices; cols = unique col indices
  minR, maxR = min/max rows; minC, maxC = min/max cols
  boxArea = (maxR-minR+1) * (maxC-minC+1)
  IF boxArea != LENGTH(cells): RETURN False
  RETURN minR==maxR OR minC==maxC
```

## Walkthrough

Scan grid: 20 ones, no diagonal neighbors. Each orthogonal blob of ones must be a full horizontal or vertical run; count lengths. If counts are 1×4, 2×3, 3×2, 4×1 → **valid**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Python | `validate_battlefield(field)` | Flood-fill + histogram |
