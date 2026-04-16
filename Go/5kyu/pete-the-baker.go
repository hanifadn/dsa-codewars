// Title: Pete, the baker
// Link: https://www.codewars.com/kata/525c65e51bf619685c000059
// Difficulty: 5 kyu
//
// ## Description
//
// Given recipe and available ingredient amounts (maps), return how many whole cakes you can bake.
// Missing keys in available count as 0.

package kata

import "math"

func Cakes(recipe, available map[string]int) int {
	minCakes := math.MaxInt
	empty := true
	for ingredient, need := range recipe {
		if need == 0 {
			continue
		}
		empty = false
		have := available[ingredient]
		n := have / need
		if n < minCakes {
			minCakes = n
		}
	}
	if empty {
		return 0
	}
	return minCakes
}
