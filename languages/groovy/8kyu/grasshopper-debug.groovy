/**
 * Title: Grasshopper - Debug
 * Link: https://www.codewars.com/kata/55cb854deb36f11f130000e1
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Debug celsius converter: convert Fahrenheit to Celsius with `celsius = (fahrenheit - 32) * (5/9)` and return
 * either `"{c} is freezing temperature"` or `"{c} is above freezing temperature"` depending on whether `c <= 0`.
 *
 * Groovy/Java reference uses **truncation toward zero** (`(int) celsius`), not `Math.round` — e.g. 36.666… → 36,
 * 0.555… → 0. Use `5.0d / 9.0d` for the same double conversion as the tests.
 */

class Kata {
	static String weatherInfo(double temp) {
		double celsius = (temp - 32) * (5.0d / 9.0d)
		int celsiusInt = (int) celsius
		celsiusInt <= 0
			? "${celsiusInt} is freezing temperature"
			: "${celsiusInt} is above freezing temperature"
	}
}
