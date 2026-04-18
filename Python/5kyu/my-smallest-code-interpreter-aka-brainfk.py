"""
Title: My smallest code interpreter (aka Brainf**k)
Link: https://www.codewars.com/kata/526156943dfe7ce06200063e
Difficulty: 5 kyu

## Description

Implement a Brainfuck interpreter: tape of 8-bit wrapping cells, up to 65536 cells; `>` extends the
tape or wraps the pointer to 0; `<` at position 0 wraps to the end; `,` consumes `program_input`;
`.` appends to the output. Ignore any character other than `><+-.,[]`.
"""

from dataclasses import dataclass, field

MAX_CELLS = 65536


def _build_bracket_jumps(source: str) -> dict[int, int]:
    open_stack: list[int] = []
    bracket_jumps: dict[int, int] = {}
    for idx, ch in enumerate(source):
        if ch == "[":
            open_stack.append(idx)
        elif ch == "]":
            open_at = open_stack.pop()
            bracket_jumps[open_at] = idx
            bracket_jumps[idx] = open_at
    return bracket_jumps


def _shift_right(ptr: int, cells: list[int]) -> int:
    ptr += 1
    if ptr < len(cells):
        return ptr
    if len(cells) < MAX_CELLS:
        cells.append(0)
        return ptr
    return 0


def _shift_left(ptr: int, cells: list[int]) -> int:
    return len(cells) - 1 if ptr == 0 else ptr - 1


def _increment_cell(cells: list[int], ptr: int) -> None:
    cells[ptr] = (cells[ptr] + 1) & 255


def _decrement_cell(cells: list[int], ptr: int) -> None:
    cells[ptr] = (cells[ptr] - 1) & 255


@dataclass
class _InterpreterState:
    cells: list[int] = field(default_factory=lambda: [0])
    ptr: int = 0
    ip: int = 0
    in_pos: int = 0
    out: list[str] = field(default_factory=list)


def _apply_bracket_jump(
    state: _InterpreterState,
    bracket_jumps: dict[int, int],
    *,
    if_zero: bool,
) -> None:
    """`[` uses if_zero=True; `]` uses if_zero=False."""
    ip = state.ip
    cell_is_zero = state.cells[state.ptr] == 0
    do_jump = cell_is_zero if if_zero else not cell_is_zero
    state.ip = bracket_jumps[ip] if do_jump else ip


def _execute_step(
    source: str,
    state: _InterpreterState,
    bracket_jumps: dict[int, int],
    inp: str,
) -> None:
    match source[state.ip]:
        case ">":
            state.ptr = _shift_right(state.ptr, state.cells)
        case "<":
            state.ptr = _shift_left(state.ptr, state.cells)
        case "+":
            _increment_cell(state.cells, state.ptr)
        case "-":
            _decrement_cell(state.cells, state.ptr)
        case ".":
            state.out.append(chr(state.cells[state.ptr]))
        case ",":
            state.cells[state.ptr] = ord(inp[state.in_pos])
            state.in_pos += 1
        case "[":
            _apply_bracket_jump(state, bracket_jumps, if_zero=True)
        case "]":
            _apply_bracket_jump(state, bracket_jumps, if_zero=False)
        case _:
            pass


def brain_luck(code: str, program_input: str) -> str:
    bracket_jumps = _build_bracket_jumps(code)
    state = _InterpreterState()
    while state.ip < len(code):
        _execute_step(code, state, bracket_jumps, program_input)
        state.ip += 1
    return "".join(state.out)
