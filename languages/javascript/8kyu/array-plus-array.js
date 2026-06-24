/**
 * Title: Array plus array
 * Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).
 */

function arrayPlusArray(arr1, arr2) {
  return arr1.concat(arr2).reduce((sum, n) => sum + n, 0);
}
