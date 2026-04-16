/**
 * Title: If you can't sleep, just count sheep!!
 * Link: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Given a non-negative integer `n`, return a string `"1 sheep...2 sheep...n sheep..."`.
 * For `n === 0`, return an empty string.
 */

function countSheep(n) {
  return Array.from({ length: n }, (_, i) => `${i + 1} sheep...`).join('');
}
