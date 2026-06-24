/**
 * Title: Array plus array
 * Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).
 */

#include <stddef.h>

long long arr_plus_arr(const int a[/* na */], const int b[/* nb */], size_t na, size_t nb) {
  long long sum = 0;
  for (size_t i = 0; i < na; i++) {
    sum += a[i];
  }
  for (size_t i = 0; i < nb; i++) {
    sum += b[i];
  }
  return sum;
}
