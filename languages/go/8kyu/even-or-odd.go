// Title: Even or Odd
// Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
// Difficulty: 8 kyu
//
// ## Description
//
// Return "Even" for even integers and "Odd" for odd integers.

package kata

func EvenOrOdd(number int) string {
	if number%2 == 0 {
		return "Even"
	}
	return "Odd"
}
