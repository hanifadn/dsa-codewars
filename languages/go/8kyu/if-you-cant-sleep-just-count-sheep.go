// Title: If you can't sleep, just count sheep!!
// Link: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
// Difficulty: 8 kyu
//
// ## Description
//
// Given a non-negative integer n, return a string "1 sheep...2 sheep...n sheep...".
// For n == 0, return an empty string.

package kata

import (
	"strconv"
	"strings"
)

func countSheep(num int) string {
	var b strings.Builder
	for i := 1; i <= num; i++ {
		b.WriteString(strconv.Itoa(i))
		b.WriteString(" sheep...")
	}
	return b.String()
}