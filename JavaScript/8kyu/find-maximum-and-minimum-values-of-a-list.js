/**
 * Title: Find Maximum and Minimum Values of a List
 * Link: https://www.codewars.com/kata/577a98a6ae28071780000989
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Implement two functions that receive a list of integers and return the smallest and largest
 * number respectively. The input is never empty.
 *
 * ## Examples (Input -> Output)
 *
 * - `[4,6,2,1,9,63,-134,566]` → max = 566, min = -134
 * - `[-52, 56, 30, 29, -54, 0, -110]` → min = -110, max = 56
 * - `[42, 54, 65, 87, 0]` → min = 0, max = 87
 * - `[5]` → min = 5, max = 5
 */

function min(list) {
  return Math.min(...list);
}

function max(list) {
  return Math.max(...list);
}
