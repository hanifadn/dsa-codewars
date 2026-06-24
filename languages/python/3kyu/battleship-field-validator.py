"""
Title: Battleship field validator
Link: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
Difficulty: 3 kyu

## Description

Decide whether a 10×10 grid is a legal Battleship deployment. Cells are `0` (water) or `1` (ship). The fleet is
exactly one length-4 ship, two length-3 ships, three length-2 ships, and four length-1 ships (20 occupied cells
in total). Each ship is a straight horizontal or vertical segment. Different ships must not touch, **including
diagonally** (only orthogonal adjacency is allowed within the same ship).
"""

from __future__ import annotations

from collections.abc import Sequence

Battlefield = list[list[int]]

GRID_SIZE = 10
REQUIRED_SHIP_CELLS = 20

EXPECTED_SHIPS_BY_LENGTH: dict[int, int] = {4: 1, 3: 2, 2: 3, 1: 4}

ORTHOGONAL_DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def validate_battlefield(field):
    if not _is_square_grid(field, GRID_SIZE):
        return False
    if _count_occupied_cells(field) != REQUIRED_SHIP_CELLS:
        return False
    if _has_touching_ships_diagonally(field):
        return False
    histogram = _histogram_of_straight_ships(field)
    return histogram is not None and histogram == EXPECTED_SHIPS_BY_LENGTH


def _is_square_grid(field: Battlefield, size: int) -> bool:
    if len(field) != size:
        return False
    return all(len(row) == size for row in field)


def _count_occupied_cells(field: Battlefield) -> int:
    return sum(sum(row) for row in field)


def _has_touching_ships_diagonally(field: Battlefield) -> bool:
    """Return True if any two ship cells from different ships share a diagonal neighbor."""
    for row in range(1, GRID_SIZE):
        for col in range(GRID_SIZE):
            if not field[row][col]:
                continue
            if col > 0 and field[row - 1][col - 1]:
                return True
            if col < GRID_SIZE - 1 and field[row - 1][col + 1]:
                return True
    return False


def _histogram_of_straight_ships(field: Battlefield) -> dict[int, int] | None:
    """Build a length → count map for each orthogonal connected component, or None if a component is invalid."""
    visited = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    histogram: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}

    for start_row in range(GRID_SIZE):
        for start_col in range(GRID_SIZE):
            if not field[start_row][start_col] or visited[start_row][start_col]:
                continue

            ship_cells = _collect_orthogonal_component(
                field, visited, start_row, start_col
            )
            ship_length = len(ship_cells)
            if ship_length not in EXPECTED_SHIPS_BY_LENGTH:
                return None
            if not _is_straight_line_segment(ship_cells):
                return None
            histogram[ship_length] += 1

    return histogram


def _collect_orthogonal_component(
    field: Battlefield,
    visited: list[list[bool]],
    start_row: int,
    start_col: int,
) -> list[tuple[int, int]]:
    stack = [(start_row, start_col)]
    visited[start_row][start_col] = True
    cells: list[tuple[int, int]] = []

    while stack:
        row, col = stack.pop()
        cells.append((row, col))
        for delta_row, delta_col in ORTHOGONAL_DELTAS:
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            if not _in_bounds(neighbor_row, neighbor_col):
                continue
            if not field[neighbor_row][neighbor_col] or visited[neighbor_row][neighbor_col]:
                continue
            visited[neighbor_row][neighbor_col] = True
            stack.append((neighbor_row, neighbor_col))

    return cells


def _in_bounds(row: int, col: int) -> bool:
    return 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE


def _is_straight_line_segment(cells: Sequence[tuple[int, int]]) -> bool:
    """True iff all cells lie on one row or one column and form a solid interval (bounding box is full)."""
    row_indices = [cell[0] for cell in cells]
    col_indices = [cell[1] for cell in cells]
    min_row, max_row = min(row_indices), max(row_indices)
    min_col, max_col = min(col_indices), max(col_indices)
    bounding_box_area = (max_row - min_row + 1) * (max_col - min_col + 1)
    if bounding_box_area != len(cells):
        return False
    return min_row == max_row or min_col == max_col
