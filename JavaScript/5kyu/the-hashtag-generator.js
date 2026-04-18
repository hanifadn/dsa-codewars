/**
 * Title: The Hashtag Generator
 * Link: https://www.codewars.com/kata/52449b062fb80683ec000024
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Build `#` + words with each word title-cased and joined without spaces. Return `false` if the input
 * is empty/whitespace-only, or the hashtag is longer than 140 characters.
 */

function generateHashtag(str) {
  const trimmed = str.trim();
  if (!trimmed) return false;
  const words = trimmed.split(/\s+/);
  const hashtag =
    '#' +
    words
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
      .join('');
  return hashtag.length > 140 ? false : hashtag;
}
