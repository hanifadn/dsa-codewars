/**
 * Title: The Hashtag Generator
 * Link: https://www.codewars.com/kata/52449b062fb80683ec000024
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Return a hashtag string: starts with `#`, each word title-cased and concatenated without spaces.
 * Return false if the input is empty/whitespace-only, or the result is longer than 140 characters.
 */

class Kata {
	static Object generateHashtag(String str) {
		if (str == null || str.trim().isEmpty()) return false
		def words = str.trim().split(/\s+/)
		def hashtag = '#' + words.collect { w ->
			w[0].toUpperCase() + w.substring(1).toLowerCase()
		}.join('')
		hashtag.length() > 140 ? false : hashtag
	}
}
