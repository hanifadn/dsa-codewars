/**
 * Title: Grasshopper - Debug
 * Link: https://www.codewars.com/kata/55cb854deb36f11f130000e1
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Debug celsius converter: convert Fahrenheit to Celsius with `celsius = (fahrenheit - 32) * (5/9)` and return
 * either `"{c} is freezing temperature"` or `"{c} is above freezing temperature"` depending on whether `c <= 0`.
 */

function weatherInfo(temp) {
  const celsius = (temp - 32) * (5 / 9);
  return celsius <= 0
    ? `${celsius} is freezing temperature`
    : `${celsius} is above freezing temperature`;
}
