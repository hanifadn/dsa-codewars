/**
 * Title: Invert values
 * Link: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Given a set of integers, return the additive inverse of each (negate every element).
 * Do not mutate the input array.
 *
 * ## Examples
 *
 * `[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]`
 * `[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]`
 * `[] --> []`
 */

function invert(array) {
  return array.map((x) => -x);
}
