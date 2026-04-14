/**
 * Title: You're a square!
 * Link: https://www.codewars.com/kata/54c27a33fb7da0db0100040e
 * Difficulty: 7 kyu
 *
 * ## Description
 *
 * Given an integral number, determine if it's a square number (perfect square): an integer
 * that is the square of some integer.
 *
 * ## Examples
 *
 * -1 -> false
 *  0 -> true
 *  3 -> false
 *  4 -> true
 * 25 -> true
 * 26 -> false
 */

class Kata {
	static boolean isSquare(int n) {
		if (n < 0)
			return false
		int floorSqrt = (int) Math.sqrt(n)
		floorSqrt * floorSqrt == n
	}
}
