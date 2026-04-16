// Title: Tortoise racing
// Link: https://www.codewars.com/kata/55e2adece53b4cdcb900006c
// Difficulty: 6 kyu
//
// ## Description
//
// Tortoise A has speed v1 and tortoise B has speed v2 (feet per hour). When B starts, A has a lead of
// g feet. How long until B catches A? Return hour, min, sec as a [3]int using whole seconds (floor).
// If v1 >= v2, return [-1, -1, -1].

package kata

func Race(v1, v2, g int) [3]int {
	if v1 >= v2 {
		return [3]int{-1, -1, -1}
	}
	totalSeconds := g * 3600 / (v2 - v1)
	h := totalSeconds / 3600
	m := (totalSeconds % 3600) / 60
	s := totalSeconds % 60
	return [3]int{h, m, s}
}
