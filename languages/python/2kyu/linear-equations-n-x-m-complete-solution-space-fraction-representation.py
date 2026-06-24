"""
Title: Linear equations N x M, complete solution space, fraction representation
Link: https://www.codewars.com/kata/56464cf3f982b2e10d000015
Difficulty: 2 kyu

## Description

Solve N×M linear systems over ℚ; return the complete solution in reduced fractions as a string:
`SOL=(...)` or `SOL=NONE`, or particular + sum of `qi * (homogeneous basis)`.
"""

from __future__ import annotations

from fractions import Fraction

_Z = Fraction(0, 1)
_ONE = Fraction(1, 1)


def _parse_frac(tok: str) -> Fraction:
    tok = tok.strip()
    if "/" in tok:
        num, den = tok.split("/", 1)
        return Fraction(int(num.strip()), int(den.strip()))
    return Fraction(int(tok), 1)


def _parse_matrix(s: str) -> list[list[Fraction]]:
    out: list[list[Fraction]] = []
    for ln in s.strip().splitlines():
        ln = ln.strip()
        if not ln:
            continue
        parts = [p for p in ln.split() if p]
        if not parts:
            continue
        out.append([_parse_frac(p) for p in parts])
    return out


def _pad_row_to_width(row: list[Fraction], w: int) -> list[Fraction]:
    if len(row) == w:
        return row
    if len(row) > w:
        return row[:w]
    padded = list(row)
    while len(padded) < w:
        padded.insert(len(padded) - 1, _Z)
    return padded


def _normalize_rows(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    """Match first row width: truncate longer rows; pad shorter with 0 coeffs before RHS."""
    if not rows:
        return rows
    w = len(rows[0])
    return [_pad_row_to_width(r, w) for r in rows]


def _aug_nx(a: list[list[Fraction]]) -> int:
    """Number of variables (last column index in augmented matrix)."""
    return len(a[0]) - 1


def _find_pivot_row(a: list[list[Fraction]], c: int, r0: int) -> int | None:
    nr = len(a)
    for i in range(r0, nr):
        if a[i][c] != 0:
            return i
    return None


def _scale_pivot_row(a: list[list[Fraction]], pr: int, c: int) -> None:
    nx = _aug_nx(a)
    inv = a[pr][c]
    for j in range(nx + 1):
        a[pr][j] /= inv


def _eliminate_other_rows(a: list[list[Fraction]], pr: int, c: int) -> None:
    nx = _aug_nx(a)
    for i in range(len(a)):
        if i == pr or a[i][c] == 0:
            continue
        f = a[i][c]
        for j in range(nx + 1):
            a[i][j] -= f * a[pr][j]


def _gauss_jordan(aug: list[list[Fraction]]) -> list[list[Fraction]]:
    """RREF of augmented [A|b]; last column is RHS (index nx)."""
    nx = _aug_nx(aug)
    a = [row[:] for row in aug]
    pr = 0
    for c in range(nx):
        ir = _find_pivot_row(a, c, pr)
        if ir is None:
            continue
        a[pr], a[ir] = a[ir], a[pr]
        _scale_pivot_row(a, pr, c)
        _eliminate_other_rows(a, pr, c)
        pr += 1
    return a


def _first_nz(row: list[Fraction], nx: int) -> int | None:
    for j in range(nx):
        if row[j] != 0:
            return j
    return None


def _coeffs_zero(row: list[Fraction], nx: int) -> bool:
    return _first_nz(row, nx) is None


def _inconsistent(rref: list[list[Fraction]], nx: int) -> bool:
    for row in rref:
        if _coeffs_zero(row, nx) and row[nx] != 0:
            return True
    return False


def _particular_from_rref(rref: list[list[Fraction]], nx: int) -> list[Fraction]:
    x0 = [_Z] * nx
    for row in rref:
        if _coeffs_zero(row, nx):
            continue
        jc = _first_nz(row, nx)
        if jc is None or row[jc] != 1:
            continue
        x0[jc] = row[nx]
    return x0


def _rref_coeff_only(coef: list[list[Fraction]]) -> list[list[Fraction]]:
    """RREF of coefficient matrix with dummy RHS column of zeros."""
    nr = len(coef)
    aug = [coef[i] + [_Z] for i in range(nr)]
    return _gauss_jordan(aug)


def _pivot_set_hom(rh: list[list[Fraction]], nx: int) -> set[int]:
    piv = set()
    for row in rh:
        j = _first_nz(row, nx)
        if j is not None:
            piv.add(j)
    return piv


def _free_cols(nx: int, piv: set[int]) -> list[int]:
    return [j for j in range(nx) if j not in piv]


def _null_basis_vec(rh: list[list[Fraction]], nx: int, jf: int) -> list[Fraction]:
    v = [_Z] * nx
    v[jf] = _ONE
    for row in rh:
        jp = _first_nz(row, nx)
        if jp is None or jp == jf:
            continue
        v[jp] = -row[jf]
    return v


def _fmt_vec(v: list[Fraction]) -> str:
    return "(" + "; ".join(str(x) for x in v) + ")"


def _format_sol_string(x0: list[Fraction], basis: list[list[Fraction]]) -> str:
    head = "SOL=" + _fmt_vec(x0)
    if not basis:
        return head
    tail = "".join(f" + q{i} * {_fmt_vec(u)}" for i, u in enumerate(basis, start=1))
    return head + tail


def solve(s: str) -> str:
    rows = _normalize_rows(_parse_matrix(s))
    if not rows:
        return "SOL=NONE"

    nr, w = len(rows), len(rows[0])
    nx = w - 1
    rref = _gauss_jordan(rows)
    if _inconsistent(rref, nx):
        return "SOL=NONE"

    x0 = _particular_from_rref(rref, nx)
    coef = [[rows[i][j] for j in range(nx)] for i in range(nr)]
    rh = _rref_coeff_only(coef)
    piv_h = _pivot_set_hom(rh, nx)
    free_j = _free_cols(nx, piv_h)
    basis = [_null_basis_vec(rh, nx, jf) for jf in free_j]

    return _format_sol_string(x0, basis)


Solve = solve
