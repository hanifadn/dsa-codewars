/**
 * Title: Moving Zeros to the End
 * Link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
 *
 * **Example**:
 * ```javascript
 * moveZeros([false, 1, 0, 1, 2, 0, 1, 3, "a"]) // returns [false, 1, 1, 2, 1, 3, "a", 0, 0]
 * ```
 */

function moveZeros(arr) {
  const nonZeros = arr.filter(item => item !== 0);
  const zeros = arr.filter(item => item === 0);
  return [...nonZeros, ...zeros];
}