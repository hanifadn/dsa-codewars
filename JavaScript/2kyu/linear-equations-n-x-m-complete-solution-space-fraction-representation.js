/**
 * Title: Linear equations N x M, complete solution space, fraction representation
 * Link: https://www.codewars.com/kata/56464cf3f982b2e10d000015
 * Difficulty: 2 kyu
 *
 * ## Description
 *
 * Solve linear systems over ℚ; return `SOL=(...)` / `SOL=NONE` / parametric solution with `qi`.
 */

function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b !== 0n) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}

class Fr {
  constructor(n, d = 1n) {
    if (d === 0n) throw new Error('divide by zero');
    let sign = 1n;
    if (n < 0n) {
      sign = -sign;
      n = -n;
    }
    if (d < 0n) {
      sign = -sign;
      d = -d;
    }
    const g = gcd(n, d);
    n = (n / g) * sign;
    d = d / g;
    this.n = n;
    this.d = d;
  }

  static fromInt(x) {
    return new Fr(BigInt(x), 1n);
  }

  add(o) {
    return new Fr(this.n * o.d + o.n * this.d, this.d * o.d);
  }

  sub(o) {
    return new Fr(this.n * o.d - o.n * this.d, this.d * o.d);
  }

  mul(o) {
    return new Fr(this.n * o.n, this.d * o.d);
  }

  div(o) {
    return new Fr(this.n * o.d, this.d * o.n);
  }

  neg() {
    return new Fr(-this.n, this.d);
  }

  eq(o) {
    return this.n * o.d === o.n * this.d;
  }

  isZero() {
    return this.n === 0n;
  }

  toString() {
    return this.d === 1n ? `${this.n}` : `${this.n}/${this.d}`;
  }
}

const FR0 = new Fr(0n, 1n);
const FR1 = new Fr(1n, 1n);

function parseFrac(token) {
  const t = token.trim();
  const slash = t.indexOf('/');
  if (slash !== -1) {
    const num = t.slice(0, slash).trim();
    const den = t.slice(slash + 1).trim();
    return new Fr(BigInt(num), BigInt(den));
  }
  return Fr.fromInt(t);
}

function parseMatrix(s) {
  return s
    .trim()
    .split(/\r?\n/)
    .map((line) =>
      line
        .trim()
        .split(/\s+/)
        .filter((t) => t.length > 0)
        .map(parseFrac)
    )
    .filter((row) => row.length > 0);
}

function normalizeRows(rows) {
  if (rows.length === 0) return rows;
  const w = rows[0].length;
  return rows.map((row) => {
    if (row.length === w) return row;
    if (row.length > w) return row.slice(0, w);
    const padded = row.slice();
    while (padded.length < w) {
      padded.splice(padded.length - 1, 0, FR0);
    }
    return padded;
  });
}

function cloneAug(aug) {
  return aug.map((row) => row.map((x) => new Fr(x.n, x.d)));
}

/** @returns row index or null */
function findPivotRow(a, c, r0, m) {
  for (let i = r0; i < m; i++) {
    if (!a[i][c].isZero()) return i;
  }
  return null;
}

function swapRows(a, i, j) {
  [a[i], a[j]] = [a[j], a[i]];
}

function scalePivotToOne(a, pr, c, nx) {
  const inv = a[pr][c];
  for (let j = 0; j <= nx; j++) {
    a[pr][j] = a[pr][j].div(inv);
  }
}

function eliminateOtherRows(a, pr, c, nx) {
  const m = a.length;
  for (let i = 0; i < m; i++) {
    if (i === pr || a[i][c].isZero()) continue;
    const f = a[i][c];
    for (let j = 0; j <= nx; j++) {
      a[i][j] = a[i][j].sub(f.mul(a[pr][j]));
    }
  }
}

function gaussJordan(aug) {
  const m = aug.length;
  const nx = aug[0].length - 1;
  const a = cloneAug(aug);
  let pr = 0;
  for (let c = 0; c < nx; c++) {
    const ir = findPivotRow(a, c, pr, m);
    if (ir === null) continue;
    swapRows(a, pr, ir);
    scalePivotToOne(a, pr, c, nx);
    eliminateOtherRows(a, pr, c, nx);
    pr += 1;
  }
  return a;
}

function firstNZ(row, nx) {
  for (let j = 0; j < nx; j++) {
    if (!row[j].isZero()) return j;
  }
  return -1;
}

function coeffsZero(row, nx) {
  return firstNZ(row, nx) === -1;
}

function inconsistent(rref, nx) {
  for (const row of rref) {
    if (coeffsZero(row, nx) && !row[nx].isZero()) return true;
  }
  return false;
}

function particularFromRref(rref, nx) {
  const x0 = Array.from({ length: nx }, () => FR0);
  for (const row of rref) {
    if (coeffsZero(row, nx)) continue;
    const jc = firstNZ(row, nx);
    if (jc < 0 || !row[jc].eq(FR1)) continue;
    x0[jc] = row[nx];
  }
  return x0;
}

function rrefCoeffOnly(A) {
  const aug = A.map((row) => row.slice().concat(FR0));
  return gaussJordan(aug);
}

function pivotCols(Rh, nx) {
  const piv = new Set();
  for (const row of Rh) {
    const j = firstNZ(row, nx);
    if (j !== -1) piv.add(j);
  }
  return piv;
}

function freeCols(nx, piv) {
  const out = [];
  for (let j = 0; j < nx; j++) {
    if (!piv.has(j)) out.push(j);
  }
  return out;
}

function nullBasisVec(Rh, nx, jf) {
  const v = Array.from({ length: nx }, () => FR0);
  v[jf] = FR1;
  for (const row of Rh) {
    const jp = firstNZ(row, nx);
    if (jp < 0 || jp === jf) continue;
    v[jp] = row[jf].neg();
  }
  return v;
}

function fmtVec(v) {
  return '(' + v.map((x) => x.toString()).join('; ') + ')';
}

function formatSolString(x0, basis) {
  const head = 'SOL=' + fmtVec(x0);
  if (basis.length === 0) return head;
  return head + basis.map((vec, i) => ` + q${i + 1} * ${fmtVec(vec)}`).join('');
}

function solve(s) {
  const rows = normalizeRows(parseMatrix(s));
  if (rows.length === 0) return 'SOL=NONE';

  const nx = rows[0].length - 1;
  const rref = gaussJordan(rows);
  if (inconsistent(rref, nx)) return 'SOL=NONE';

  const x0 = particularFromRref(rref, nx);
  const A = rows.map((row) => row.slice(0, nx));
  const Rh = rrefCoeffOnly(A);
  const pivH = pivotCols(Rh, nx);
  const freeJ = freeCols(nx, pivH);
  const basis = freeJ.map((jf) => nullBasisVec(Rh, nx, jf));

  return formatSolString(x0, basis);
}

const Solve = solve;

if (typeof module !== 'undefined' && module != null) {
  module.exports = solve;
  module.exports.solve = solve;
  module.exports.Solve = solve;
}
