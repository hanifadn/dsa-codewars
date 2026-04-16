// Title: Invert values
// Link: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
// Difficulty: 8 kyu
//
// ## Description
//
// Given a slice of integers, return a new slice with each value negated (additive inverse).
// Do not mutate the input slice.
//
// ## Examples
//
// [1, 2, 3, 4, 5]   --> [-1, -2, -3, -4, -5]
// [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
// []                --> []

package kata

func Invert(arr []int) []int {
	out := make([]int, len(arr))
	for i, v := range arr {
		out[i] = -v
	}
	return out
}
