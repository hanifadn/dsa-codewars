"""
Title: 4 By 4 Skyscrapers
Link: https://www.codewars.com/kata/5671d975d81d6c1c87000022
Difficulty: 4 kyu

## Description

Solve a 4×4 skyscraper puzzle: place heights 1–4 in each cell so every row and column is a permutation of 1–4.
Clues around the grid (16 values, clockwise; `0` means unknown) give how many buildings are visible from that
direction; taller buildings hide shorter ones behind them.
"""

from __future__ import annotations

import itertools
from collections.abc import Iterable, Sequence

Row4 = tuple[int, int, int, int]
Grid = list[list[int]]

SIZE = 4


def count_visible(heights: Iterable[int]) -> int:
    tallest = 0
    seen = 0
    for height in heights:
        if height <= tallest:
            continue
        tallest = height
        seen += 1
    return seen


def row_fits_edge_clues(candidate: Row4, clue_left: int, clue_right: int) -> bool:
    left_ok = clue_left == 0 or count_visible(candidate) == clue_left
    right_ok = clue_right == 0 or count_visible(reversed(candidate)) == clue_right
    return left_ok and right_ok


def row_options_for_index(row: int, clues: Sequence[int]) -> list[Row4]:
    clue_left = clues[15 - row]
    clue_right = clues[4 + row]
    return [
        c
        for c in itertools.permutations((1, 2, 3, 4))
        if row_fits_edge_clues(c, clue_left, clue_right)
    ]


def column_fits_edge_clues(column: list[int], clue_top: int, clue_bottom: int) -> bool:
    top_ok = clue_top == 0 or count_visible(column) == clue_top
    bottom_ok = clue_bottom == 0 or count_visible(reversed(column)) == clue_bottom
    return top_ok and bottom_ok


def columns_match_top_bottom(grid: Grid, clues: Sequence[int]) -> bool:
    for col in range(SIZE):
        column = [grid[r][col] for r in range(SIZE)]
        if not column_fits_edge_clues(column, clues[col], clues[8 + (3 - col)]):
            return False
    return True


def column_clashes_with_above(grid: Grid, row: int, choice: Sequence[int]) -> bool:
    for col in range(SIZE):
        height = choice[col]
        for above in range(row):
            if grid[above][col] == height:
                return True
    return False


def assign_row(grid: Grid, row: int, choice: Sequence[int]) -> None:
    for col in range(SIZE):
        grid[row][col] = choice[col]


def clone_rows(grid: Grid) -> Grid:
    return [line[:] for line in grid]


def dfs(
    row: int,
    grid: Grid,
    rows_by_depth: list[list[Row4]],
    clues: Sequence[int],
) -> Grid | None:
    if row == SIZE:
        return clone_rows(grid) if columns_match_top_bottom(grid, clues) else None
    for choice in rows_by_depth[row]:
        if column_clashes_with_above(grid, row, choice):
            continue
        assign_row(grid, row, choice)
        solved = dfs(row + 1, grid, rows_by_depth, clues)
        if solved is not None:
            return solved
    return None


def solve_puzzle (clues: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    rows_by_depth = [row_options_for_index(i, clues) for i in range(SIZE)]
    grid: Grid = [[0] * SIZE for _ in range(SIZE)]
    result = dfs(0, grid, rows_by_depth, clues)
    if result is None:
        raise ValueError("no solution")
    # shape: ((…), (…), (…), (…)) — one tuple per row, not a fixed pattern
    return tuple(tuple(r) for r in result)
