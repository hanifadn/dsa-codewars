# Matrix Determinant

| Field | Value |
|-------|-------|
| Slug | matrix-determinant |
| Kyu | 4 |
| Link | https://www.codewars.com/kata/52a382ee44408cea2500074c |
| Status | backfilled |
| Reference | languages/python/4kyu/matrix-determinant.py |

## Summary

Compute the determinant of an N×N square matrix using Laplace (cofactor) expansion along the first row.

## Input / Output

- **Input:** `matrix` — square 2D array of numbers (integers in tests).
- **Output:** Scalar determinant.
- **Constraints:** N ≥ 1; matrix is square.

## Examples

| Input | Output |
|-------|--------|
| `[[1]]` | 1 |
| `[[1,2],[3,4]]` | -1 |
| `[[1,2,3],[4,5,6],[7,8,9]]` | 0 |

## Edge Cases

- 1×1 matrix → single element.
- 2×2 uses ad hoc formula: `a*d - b*c`.
- Sign alternates by column index in first-row expansion.

## Approach

- **Algorithm:** Recursive Laplace expansion: `det(M) = Σ_j (-1)^j * M[0][j] * det(minor(M,0,j))`.
- **Time:** O(n!) naive recursion; acceptable for kata sizes
- **Space:** O(n²) for minors per recursion level

## Behavioral Contract

- `minor(matrix, row, col)` removes row `row` and column `col`.
- Cofactor sign: add at even column index, subtract at odd (`j % 2`).
- Integer matrices yield integer determinants.

## Pseudocode

```text
FUNCTION minor(matrix, row, col):
  RETURN [
    [matrix[i][j] for j != col]
    for i != row
  ]

FUNCTION determinant(matrix):
  n = NUMBER OF ROWS(matrix)
  IF n == 1:
    RETURN matrix[0][0]
  IF n == 2:
    RETURN matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

  det = 0
  FOR j FROM 0 TO n-1:
    term = matrix[0][j] * determinant(minor(matrix, 0, j))
    IF j IS EVEN:
      det = det + term
    ELSE:
      det = det - term
  RETURN det
```

## Walkthrough

For `[[1,2],[3,4]]`:

1. n = 2 → `1*4 - 2*3` = 4 - 6 = **-1**.

For 3×3, expand on row 0: three 2×2 minors with alternating signs.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Go | `Determinant` | |
| JavaScript | `determinant` | |
| Python | `determinant(matrix)` | Laplace recursion |
