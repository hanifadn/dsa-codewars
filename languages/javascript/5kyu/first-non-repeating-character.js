/**
 * Title: First Non-Repeating Character
 * Link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
 * Difficulty: 5 kyu
 *
 * ## Description
 *
 * Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.
 *
 * For example, if given the input `"stress"`, the function should return `'t'`, since the letter `t` only occurs once in the string, and occurs first in the string.
 *
 * As an added challenge, upper- and lowercase characters are considered the same character, but the function should return the correct case for the initial character. For example, the input `"sTreSS"` should return `"T"`.
 *
 * If a string contains only repeating characters, return an empty string (`""`).
 *
 * > **Note**: despite its name in some languages, your function should handle any Unicode codepoint.
 *
 * **Examples**:
 * ```
 * "@#@@*"    --> "#"
 * "かか何"   --> "何"
 * "🐐🦊🐐" --> "🦊"
 * ```
 */

function firstNonRepeatingLetter(s) {
  const lower = s.toLowerCase();
  const freq = {};

  // Count occurrences (case-insensitive)
  for (const char of lower) {
    freq[char] = (freq[char] || 0) + 1;
  }

  // Find first non-repeating character (preserve original case)
  let i = 0;
  for (const char of lower) {
    if (freq[char] === 1) {
      return s[i];
    }
    i++;
  }

  return '';
}