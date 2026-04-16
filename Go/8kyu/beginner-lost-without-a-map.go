// Title: Beginner - Lost Without a Map
// Link: https://www.codewars.com/kata/57f781872e3d8ca2a000007e
// Difficulty: 8 kyu
//
// ## Description
//
// Given an array of integers, return a new array with each value doubled.
//
// ## Examples
//
// [1, 2, 3] --> [2, 4, 6]

package kata

func Maps(arr []int) []int {
	out := make([]int, len(arr))
	for i, v := range arr {
		out[i] = v * 2
	}
	return out
}
