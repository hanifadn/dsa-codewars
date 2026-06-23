"""
Title: Matrix Determinant
Link: https://www.codewars.com/kata/52a382ee44408cea2500074c
Difficulty: 4 kyu

## Description

Return the determinant of an N×N square matrix via Laplace expansion along the first row:
det(M) = Σ (-1)^j * M[0][j] * det(minor(M, 0, j)).
"""


def minor(matrix, row, col):
    return [
        [value for j, value in enumerate(line) if j != col]
        for i, line in enumerate(matrix)
        if i != row
    ]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        val = matrix[0][j] * determinant(minor(matrix, 0, j))
        det += val if j % 2 == 0 else -val
    return det
