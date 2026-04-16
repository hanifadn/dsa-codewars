/**
 * Title: Binary Addition
 * Link: https://www.codewars.com/kata/551f37452ff852b7bd000139
 * Difficulty: 7 kyu
 *
 * ## Description
 *
 * Add two integers and return their sum as a binary string.
 *
 * ## Examples
 *
 * - `1, 1` → `"10"`
 * - `5, 9` → `"1110"`
 */

class Kata {
	static String addBinary(long a, long b) {
		Long.toBinaryString(a + b)
	}
}
