/**
 * Title: My smallest code interpreter (aka Brainf**k)
 * Link: https://www.codewars.com/kata/526156943dfe7ce06200063e
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Implement a Brainfuck interpreter: tape of 8-bit wrapping cells, up to 65536 cells; `>` extends
 * the tape or wraps the pointer to 0; `<` at position 0 wraps to the end; `,` consumes `input`;
 * `.` appends to the output. Ignore any characters other than `><+-.,[]`.
 */

const MAX_CELLS = 65536;

function buildBracketJumps(source) {
  const openStack = [];
  const jumps = new Map();
  for (let i = 0; i < source.length; i++) {
    const ch = source[i];
    if (ch === '[') openStack.push(i);
    else if (ch === ']') {
      const openAt = openStack.pop();
      jumps.set(openAt, i);
      jumps.set(i, openAt);
    }
  }
  return jumps;
}

function shiftRight(ptr, cells) {
  ptr += 1;
  if (ptr < cells.length) return ptr;
  if (cells.length < MAX_CELLS) {
    cells.push(0);
    return ptr;
  }
  return 0;
}

function shiftLeft(ptr, cells) {
  return ptr === 0 ? cells.length - 1 : ptr - 1;
}

function nextBracketIp(s, ifZero) {
  const cellIsZero = s.cells[s.ptr] === 0;
  const doJump = ifZero ? cellIsZero : !cellIsZero;
  return doJump ? s.jumps.get(s.ip) : s.ip;
}

const tapeOps = {
  '>': (m) => {
    m.ptr = shiftRight(m.ptr, m.cells);
  },
  '<': (m) => {
    m.ptr = shiftLeft(m.ptr, m.cells);
  },
  '+': (m) => {
    m.cells[m.ptr] = (m.cells[m.ptr] + 1) & 255;
  },
  '-': (m) => {
    m.cells[m.ptr] = (m.cells[m.ptr] - 1) & 255;
  },
};

function runStep(m, code, input) {
  const ch = code[m.ip];
  const tapeOp = tapeOps[ch];
  if (tapeOp) {
    tapeOp(m);
    return;
  }
  if (ch === '.') {
    m.out += String.fromCharCode(m.cells[m.ptr]);
    return;
  }
  if (ch === ',') {
    m.cells[m.ptr] = input.charCodeAt(m.inPos++);
    return;
  }
  if (ch === '[') {
    m.ip = nextBracketIp(
      { cells: m.cells, ptr: m.ptr, ip: m.ip, jumps: m.jumps },
      true,
    );
    return;
  }
  if (ch === ']') {
    m.ip = nextBracketIp(
      { cells: m.cells, ptr: m.ptr, ip: m.ip, jumps: m.jumps },
      false,
    );
  }
}

function brainLuck(code, input) {
  const m = {
    jumps: buildBracketJumps(code),
    cells: [0],
    ptr: 0,
    ip: 0,
    inPos: 0,
    out: '',
  };
  while (m.ip < code.length) {
    runStep(m, code, input);
    m.ip += 1;
  }
  return m.out;
}
