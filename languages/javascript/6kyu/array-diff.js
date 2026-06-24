/**
 * Title: Array.diff
 * Link: https://www.codewars.com/kata/523f5d21c841566fde000009
 * Difficulty: 6 kyu
 *
 * ## Description
 *
 * Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (`a`) that are present in the second list (`b`). The order of elements in the first list should be preserved in the result.
 *
 * **Examples**:
 * ```javascript
 * arrayDiff([1, 2], [1]) // returns [2]
 * arrayDiff([1, 2, 2, 2, 3], [2]) // returns [1, 3]
 * ```
 */

function arrayDiff(a, b) {
  return a.filter(item => !b.includes(item));
}