/**
 * Title: Sum Arrays
 * Link: https://www.codewars.com/kata/53dc54212259ed3d4f00071c
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of the numbers in the array. The array may be empty (return `0`) or contain
 * negative and floating‑point values.
 *
 * ## Examples
 *
 * - `[1, 5.2, 4, 0, -1]` → `9.2`
 * - `[-2.398]` → `-2.398`
 * - `[]` → `0`
 */

function sum(numbers) {
  return numbers.reduce((acc, n) => acc + n, 0);
}
