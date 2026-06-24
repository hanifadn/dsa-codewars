/**
 * Title: Counting Duplicates
 * Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 * Difficulty: 6 kyu
 *
 * ## Description
 *
 * Return the count of distinct case-insensitive alphabetic characters and numeric digits
 * that occur more than once in the input string. The input contains only letters and digits.
 *
 * ## Examples
 *
 * - "abcde" -> 0
 * - "aabbcde" -> 2 ('a' and 'b')
 * - "aabBcde" -> 2
 * - "indivisibility" -> 1 ('i')
 * - "Indivisibilities" -> 2 ('i' and 's')
 * - "aA11" -> 2 ('a' and '1')
 * - "ABBA" -> 2 ('A' and 'B')
 */

class Kata {
	static Integer duplicateCount(String text) {
		text.toLowerCase().toList().countBy { it }.values().count { it > 1 }
	}
}
