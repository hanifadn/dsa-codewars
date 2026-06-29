# Linear equations N x M, complete solution space, fraction representation

| Field | Value |
|-------|-------|
| Slug | linear-equations-n-x-m-complete-solution-space-fraction-representation |
| Kyu | 2 |
| Link | https://www.codewars.com/kata/56464cf3f982b2e10d000015 |
| Status | backfilled |
| Reference | languages/python/2kyu/linear-equations-n-x-m-complete-solution-space-fraction-representation.py |

## Summary

Parse an N×M linear system over ℚ given as whitespace-separated fraction tokens per row (augmented matrix: coefficients then RHS). Return the complete solution as an exact reduced-fraction string: `SOL=(x1; …; xn)` for a particular solution, optionally plus `+ q1 * (homogeneous vector) + …` for a basis of the null space. Return `SOL=NONE` if inconsistent.

## Input / Output

- **Input:** Multi-line string; each non-empty line is one equation; tokens are integers or `num/den` fractions; last token per row is the RHS constant.
- **Output:** Single string in the format above; fractions in lowest terms.
- **Constraints:** Pad shorter rows with zero coefficients before RHS to match first row width; variables count = columns − 1.

## Examples

| Input | Output |
|-------|--------|
| Unique solution system | `SOL=(1/2; -3)` |
| Underdetermined consistent system | `SOL=(0; 0) + q1 * (1; -1)` |
| `0 = 1` style inconsistency | `SOL=NONE` |
| Empty input | `SOL=NONE` |

## Edge Cases

- Rows of unequal length: pad with `0` coefficients immediately before the RHS cell.
- RREF may have free variables not appearing as pivots in the particular-solution pass.
- Homogeneous basis: one vector per free column, that coordinate = 1, pivot coords from negated RREF entries.
- Inconsistency: a row with all zero coefficients and non-zero RHS.

## Approach

- **Algorithm:** Parse to `Fraction` matrix → Gauss–Jordan RREF on augmented system → detect inconsistency → read particular solution from pivot rows → RREF coefficient-only matrix → build null-space basis for free columns → format.
- **Time:** O(n·m·min(n,m)) on fraction ops
- **Space:** O(n·m)

## Behavioral Contract

- Vector format: `(a; b; c)` with `; ` separators; fractions as `p/q` or integer `p`.
- Parameter names: `q1`, `q2`, … in order of increasing free-column index.
- Particular solution: for each RREF row with leading 1 at column j, set x[j] = RHS; others 0 unless updated.
- `SOL=NONE` for empty parse or inconsistent systems only.

## Pseudocode

```text
FUNCTION parseMatrix(s):
  FOR each non-empty line:
    tokens = split whitespace
    row = map each token to Fraction
    APPEND row
  RETURN rows

FUNCTION padRows(rows):
  w = length of rows[0]
  FOR each row: pad with 0 coeffs before RHS until length w

FUNCTION gaussJordan(aug):
  nx = number of variables (last col index)
  pr = 0
  FOR col FROM 0 TO nx-1:
    find pivot row >= pr with nonzero in col
    IF none: CONTINUE
    swap rows pr and pivot
    scale pivot row so aug[pr][col] == 1
    eliminate col in all other rows
    pr += 1
  RETURN aug

FUNCTION inconsistent(rref, nx):
  FOR each row:
    IF all coeffs 0 AND rhs != 0: RETURN True
  RETURN False

FUNCTION particular(rref, nx):
  x = vector of nx zeros
  FOR each row in rref:
    j = first nonzero col index
    IF aug[row][j] == 1:
      x[j] = rhs of row
  RETURN x

FUNCTION nullBasis(coefMatrix, nx):
  rh = gaussJordan(augment coef with zero RHS)
  pivots = set of first nonzero col per row
  freeCols = cols not in pivots
  basis = []
  FOR jf IN freeCols:
    v = zero vector; v[jf] = 1
    FOR each row in rh with pivot jp:
      v[jp] = -rh[row][jf]
    APPEND v TO basis
  RETURN basis

FUNCTION formatVec(v):
  RETURN "(" + join("; ", str each component) + ")"

FUNCTION solve(s):
  rows = padRows(parseMatrix(s))
  IF rows empty: RETURN "SOL=NONE"
  nx = width - 1
  rref = gaussJordan(rows)
  IF inconsistent(rref, nx): RETURN "SOL=NONE"
  x0 = particular(rref, nx)
  coef = coefficient columns only
  basis = nullBasis(coef, nx)
  out = "SOL=" + formatVec(x0)
  FOR i, u IN enumerate(basis, start=1):
    out += " + q" + i + " * " + formatVec(u)
  RETURN out
```

## Walkthrough

Two equations, two unknowns with unique solution: RREF yields identity on coeffs; particular reads RHS into x; no free columns → **`SOL=(…)`** only. If one free column, append **`+ q1 * (…)`** with the null-space direction.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| JavaScript | `solve` | |
| Python | `solve(s)` / `Solve` | Gauss–Jordan over Fraction |
