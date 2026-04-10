/**
 * Title: Get the Middle Character
 * Link: https://www.codewars.com/kata/56747fd5cb988479af000028
 * Difficulty: 7 kyu
 *
 * ## Description
 *
 * You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
 *
 * - If the string's length is odd, return the middle character.
 * - If the string's length is even, return the middle 2 characters.
 *
 * **Examples**:
 * ```text
 * "test"    --> "es"
 * "testing" --> "t"
 * "middle"  --> "dd"
 * "A"       --> "A"
 * ```
 */

function getMiddle(s) {
  const len = s.length;
  const mid = Math.floor(len / 2);

  return len % 2 === 0
    ? s.slice(mid - 1, mid + 1)
    : s.charAt(mid);
}