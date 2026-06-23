// Title: Matrix Determinant
// Link: https://www.codewars.com/kata/52a382ee44408cea2500074c
// Difficulty: 4 kyu
//
// ## Description
//
// Return the determinant of an N×N square matrix via Laplace expansion along the first row:
// det(M) = Σ (-1)^j * M[0][j] * det(minor(M, 0, j)).

package kata

func Determinant(matrix [][]int) int {
	n := len(matrix)
	if n == 1 {
		return matrix[0][0]
	}
	if n == 2 {
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	}
	det := 0
	for j := 0; j < n; j++ {
		val := matrix[0][j] * Determinant(minor(matrix, 0, j))
		if j%2 == 0 {
			det += val
		} else {
			det -= val
		}
	}
	return det
}

func minor(matrix [][]int, row, col int) [][]int {
	n := len(matrix)
	result := make([][]int, n-1)
	idx := 0
	for i := 0; i < n; i++ {
		if i == row {
			continue
		}
		line := make([]int, 0, n-1)
		for j := 0; j < n; j++ {
			if j == col {
				continue
			}
			line = append(line, matrix[i][j])
		}
		result[idx] = line
		idx++
	}
	return result
}
