# My Smallest Code Interpreter Aka Brainfk

| Field | Value |
|-------|-------|
| Slug | my-smallest-code-interpreter-aka-brainfk |
| Kyu | 5 |
| Link | https://www.codewars.com/kata/526156943dfe7ce06200063e |
| Status | backfilled |
| Reference | languages/python/5kyu/my-smallest-code-interpreter-aka-brainfk.py |

## Summary

Implement a Brainfuck interpreter. Execute commands on a byte tape with wrapping arithmetic, produce output from `.` instructions, and consume `program_input` for `,` instructions. Ignore any character outside `><+-.,[]`.

## Input / Output

- **Input:** `code` (program string) and `program_input` (string consumed by `,`).
- **Output:** Concatenated characters produced by `.` instructions.
- **Constraints:** Cells hold 0–255 with wrap on `+`/`-`; up to 65,536 cells; pointer wraps at tape boundaries per kata rules.

## Examples

| Input | Output |
|-------|--------|
| `"+."`, `""` | `"\x01"` (chr(1)) |
| `"+++.>++.<+++++++..+++.", ""` | `"Hi"` (typical hello-world fragment) |
| `",.", `"A"` | `"A"` |

## Edge Cases

- `>` at last cell: extend tape if under 65,536 cells, else wrap pointer to 0.
- `<` at position 0: wrap to last cell.
- `,` reads `ord` of next input char; input is guaranteed sufficient for tests.
- Unmatched brackets are not in valid test programs.
- Non-command characters are no-ops (instruction pointer still advances).

## Approach

- **Algorithm:** Precompute `[`/`]` jump map; simulate with instruction pointer, data pointer, tape array, input index, and output buffer.
- **Time:** O(instructions executed)
- **Space:** O(tape size + code length)

## Behavioral Contract

- Cell values wrap: `(value ± 1) mod 256`.
- `[`: if current cell is 0, jump to matching `]`; else fall through.
- `]`: if current cell is non-zero, jump to matching `[`; else fall through.
- Output is a string of characters from `chr(cell_value)`.

## Pseudocode

```text
FUNCTION buildBracketJumps(code):
  stack = []
  jumps = EMPTY MAP
  FOR i, ch IN ENUMERATE(code):
    IF ch == "[":
      PUSH i ON stack
    IF ch == "]":
      open = POP stack
      jumps[open] = i
      jumps[i] = open
  RETURN jumps

FUNCTION shiftRight(ptr, cells, MAX_CELLS):
  ptr = ptr + 1
  IF ptr < LENGTH(cells):
    RETURN ptr
  IF LENGTH(cells) < MAX_CELLS:
    APPEND 0 TO cells
    RETURN ptr
  RETURN 0

FUNCTION shiftLeft(ptr, cells):
  IF ptr == 0:
    RETURN LENGTH(cells) - 1
  RETURN ptr - 1

FUNCTION brainLuck(code, program_input):
  jumps = buildBracketJumps(code)
  cells = [0]
  ptr = 0
  ip = 0
  in_pos = 0
  out = []

  WHILE ip < LENGTH(code):
    ch = code[ip]
    SWITCH ch:
      ">": ptr = shiftRight(ptr, cells, 65536)
      "<": ptr = shiftLeft(ptr, cells)
      "+": cells[ptr] = (cells[ptr] + 1) MOD 256
      "-": cells[ptr] = (cells[ptr] - 1) MOD 256
      ".": APPEND CHR(cells[ptr]) TO out
      ",": cells[ptr] = ORD(program_input[in_pos]); in_pos += 1
      "[":
        IF cells[ptr] == 0:
          ip = jumps[ip]   // skip loop body
      "]":
        IF cells[ptr] != 0:
          ip = jumps[ip]   // back to [
      DEFAULT: // ignore
    ip += 1

  RETURN JOIN(out)
```

## Walkthrough

For `",."` with input `"A"`:

1. `,` sets cell[0] = ord('A') = 65.
2. `.` appends chr(65) → `"A"`.
3. Return **`"A"`**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `brainLuck` | |
| JavaScript | `brainLuck` | |
| Python | `brain_luck(code, program_input)` | Bracket pre-scan |
