/**
 * Title: Matrix Determinant
 * Link: https://www.codewars.com/kata/52a382ee44408cea2500074c
 * Difficulty: 4 kyu
 *
 * ## Description
 *
 * Return the determinant of an N×N square matrix via Laplace expansion along the first row:
 * det(M) = Σ (-1)^j * M[0][j] * det(minor(M, 0, j)).
 */

function minor(matrix, row, col) {
  return matrix
    .filter((_, i) => i !== row)
    .map((line) => line.filter((_, j) => j !== col));
}

function determinant(matrix) {
  const n = matrix.length;
  if (n === 1) return matrix[0][0];
  if (n === 2) return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];

  let det = 0;
  for (let j = 0; j < n; j++) {
    const val = matrix[0][j] * determinant(minor(matrix, 0, j));
    det += j % 2 === 0 ? val : -val;
  }
  return det;
}
