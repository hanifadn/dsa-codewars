// Title: 4 By 4 Skyscrapers
// Link: https://www.codewars.com/kata/5671d975d81d6c1c87000022
// Difficulty: 4 kyu
//
// ## Description
//
// Solve a 4×4 skyscraper puzzle: place heights 1–4 in each cell so every row and column is a permutation of 1–4.
// Clues around the grid (16 values, clockwise; 0 means unknown) give how many buildings are visible from that
// direction; taller buildings hide shorter ones behind them.

package kata

const size = 4

func countVisibleAlong(heights []int, reverse bool) int {
	tallest, seen := 0, 0
	n := len(heights)
	if n == 0 {
		return 0
	}
	idx, step := 0, 1
	if reverse {
		idx = n - 1
		step = -1
	}
	for i := 0; i < n; i++ {
		height := heights[idx]
		if height > tallest {
			tallest = height
			seen++
		}
		idx += step
	}
	return seen
}

func countVisible(heights []int) int {
	return countVisibleAlong(heights, false)
}

func countVisibleFromEnd(heights [4]int) int {
	return countVisibleAlong(heights[:], true)
}

var rowPermutations [][4]int

func init() {
	digits := [4]int{1, 2, 3, 4}
	var partial [4]int
	var generate func(int)
	generate = func(pos int) {
		if pos == size {
			snap := partial
			rowPermutations = append(rowPermutations, snap)
			return
		}
		for _, height := range digits {
			taken := false
			for j := 0; j < pos; j++ {
				if partial[j] == height {
					taken = true
					break
				}
			}
			if taken {
				continue
			}
			partial[pos] = height
			generate(pos + 1)
		}
	}
	generate(0)
}

func rowFitsEdgeClues(candidate [4]int, clueLeft, clueRight int) bool {
	leftOk := clueLeft == 0 || countVisible(candidate[:]) == clueLeft
	rightOk := clueRight == 0 || countVisibleFromEnd(candidate) == clueRight
	return leftOk && rightOk
}

func rowOptionsForIndex(row int, clues []int) [][4]int {
	clueLeft := clues[15-row]
	clueRight := clues[4+row]
	var options [][4]int
	for _, candidate := range rowPermutations {
		if rowFitsEdgeClues(candidate, clueLeft, clueRight) {
			options = append(options, candidate)
		}
	}
	return options
}

func columnFitsEdgeClues(column [4]int, clueTop, clueBottom int) bool {
	topOk := clueTop == 0 || countVisible(column[:]) == clueTop
	bottomOk := clueBottom == 0 || countVisibleFromEnd(column) == clueBottom
	return topOk && bottomOk
}

func columnsMatchTopBottom(grid *[4][4]int, clues []int) bool {
	var col [4]int
	for c := 0; c < size; c++ {
		for r := 0; r < size; r++ {
			col[r] = grid[r][c]
		}
		if !columnFitsEdgeClues(col, clues[c], clues[8+(3-c)]) {
			return false
		}
	}
	return true
}

func columnClashesWithAbove(grid *[4][4]int, row int, choice [4]int) bool {
	for c := 0; c < size; c++ {
		h := choice[c]
		for above := 0; above < row; above++ {
			if grid[above][c] == h {
				return true
			}
		}
	}
	return false
}

func dfs(row int, grid *[4][4]int, rowsByDepth [][][4]int, clues []int) bool {
	if row == size {
		return columnsMatchTopBottom(grid, clues)
	}
	for _, choice := range rowsByDepth[row] {
		if columnClashesWithAbove(grid, row, choice) {
			continue
		}
		for c := 0; c < size; c++ {
			grid[row][c] = choice[c]
		}
		if dfs(row+1, grid, rowsByDepth, clues) {
			return true
		}
	}
	return false
}

func gridToResult(g *[4][4]int) [][]int {
	backing := make([]int, size*size)
	out := make([][]int, size)
	for r := 0; r < size; r++ {
		slice := backing[r*size : (r+1)*size]
		copy(slice, g[r][:])
		out[r] = slice
	}
	return out
}

func SolvePuzzle(clues []int) [][]int {
	if len(clues) != 16 {
		return nil
	}
	rowsByDepth := make([][][4]int, size)
	for i := 0; i < size; i++ {
		rowsByDepth[i] = rowOptionsForIndex(i, clues)
		if len(rowsByDepth[i]) == 0 {
			return nil
		}
	}
	var grid [4][4]int
	if !dfs(0, &grid, rowsByDepth, clues) {
		return nil
	}
	return gridToResult(&grid)
}
