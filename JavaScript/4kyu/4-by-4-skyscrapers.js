/**
 * Title: 4 By 4 Skyscrapers
 * Link: https://www.codewars.com/kata/5671d975d81d6c1c87000022
 * Difficulty: 4 kyu
 *
 * ## Description
 *
 * Solve a 4×4 skyscraper puzzle: place heights 1–4 in each cell so every row and column is a permutation of 1–4.
 * Clues around the grid (16 values, clockwise; `0` means unknown) give how many buildings are visible from that
 * direction; taller buildings hide shorter ones behind them.
 */

const SIZE = 4;

function countVisible(heights) {
  let tallest = 0;
  let seen = 0;
  for (let i = 0; i < heights.length; i++) {
    const h = heights[i];
    if (h <= tallest) continue;
    tallest = h;
    seen++;
  }
  return seen;
}

function countVisibleFromEnd(heights) {
  return countVisible([heights[3], heights[2], heights[1], heights[0]]);
}

const ROW_PERMUTATIONS = (function buildPermutations1234() {
  const digits = [1, 2, 3, 4];
  const out = [];
  function build(chosen, remaining) {
    if (remaining.length === 0) {
      out.push(chosen.slice());
      return;
    }
    for (let i = 0; i < remaining.length; i++) {
      chosen.push(remaining[i]);
      build(chosen, remaining.filter((_, j) => j !== i));
      chosen.pop();
    }
  }
  build([], digits);
  return out;
})();

function rowFitsEdgeClues(candidate, clueLeft, clueRight) {
  const leftOk = clueLeft === 0 || countVisible(candidate) === clueLeft;
  const rightOk = clueRight === 0 || countVisibleFromEnd(candidate) === clueRight;
  return leftOk && rightOk;
}

function rowOptionsForIndex(rowIndex, clues) {
  const clueLeft = clues[15 - rowIndex];
  const clueRight = clues[4 + rowIndex];
  return ROW_PERMUTATIONS.filter((c) => rowFitsEdgeClues(c, clueLeft, clueRight));
}

function columnFitsEdgeClues(column, clueTop, clueBottom) {
  const topOk = clueTop === 0 || countVisible(column) === clueTop;
  const bottomOk = clueBottom === 0 || countVisibleFromEnd(column) === clueBottom;
  return topOk && bottomOk;
}

function columnsMatchTopBottom(board, clues) {
  for (let col = 0; col < SIZE; col++) {
    const column = [board[0][col], board[1][col], board[2][col], board[3][col]];
    const clueTop = clues[col];
    const clueBottom = clues[8 + (3 - col)];
    if (!columnFitsEdgeClues(column, clueTop, clueBottom)) return false;
  }
  return true;
}

function columnClashesWithAbove(grid, row, choice) {
  for (let col = 0; col < SIZE; col++) {
    const height = choice[col];
    for (let above = 0; above < row; above++) {
      if (grid[above][col] === height) return true;
    }
  }
  return false;
}

function assignRow(grid, row, choice) {
  for (let col = 0; col < SIZE; col++) grid[row][col] = choice[col];
}

function cloneRows(grid) {
  return grid.map((line) => line.slice());
}

function dfs(row, grid, rowsByDepth, clues) {
  if (row === SIZE) {
    return columnsMatchTopBottom(grid, clues) ? cloneRows(grid) : null;
  }
  for (const choice of rowsByDepth[row]) {
    if (columnClashesWithAbove(grid, row, choice)) continue;
    assignRow(grid, row, choice);
    const solved = dfs(row + 1, grid, rowsByDepth, clues);
    if (solved) return solved;
  }
  return null;
}

function solvePuzzle (clues) {
  const rowsByDepth = [0, 1, 2, 3].map((i) => rowOptionsForIndex(i, clues));
  const grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ];
  return dfs(0, grid, rowsByDepth, clues);
}
