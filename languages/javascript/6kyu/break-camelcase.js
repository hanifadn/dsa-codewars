/**
 * Title: Break CamelCase
 * Link: https://www.codewars.com/kata/5208f99aee097e6552000148
 * Difficulty: 6 kyu
 *
 * ## Description
 *
 * Complete the solution so that the function will break up camel casing, using a space between words.
 *
 * **Examples**:
 * ```text
 * "camelCasing"  =>  "camel Casing"
 * "identifier"   =>  "identifier"
 * ""             =>  ""
 * ```
 */

function solution(string) {
  return string.replace(/([A-Z])/g, ' $1');
}