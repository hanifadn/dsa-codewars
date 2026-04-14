/**
 * Title: Anagram Detection
 * Link: https://www.codewars.com/kata/529eef7a9194e0cbc1000255
 * Difficulty: 7 kyu
 *
 * ## Description
 *
 * An anagram is the result of rearranging the letters of a word to produce a new word.
 *
 * Note: anagrams are case insensitive.
 *
 * Complete the function to return true if the two arguments given are anagrams of each
 * other; return false otherwise.
 *
 * ## Examples
 *
 * - "foefet" is an anagram of "toffee"
 * - "Buckethead" is an anagram of "DeathCubeK"
 */

class Kata {
	static boolean isAnagram(String test, String original) {
		test.toLowerCase().toList().sort().join() == original.toLowerCase().toList().sort().join()
	}
}
