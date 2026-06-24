/**
 * Title: Beginner - Lost Without a Map
 * Link: https://www.codewars.com/kata/57f781872e3d8ca2a000007e
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Given an array of integers, return a new array with each value doubled.
 *
 * ## Examples
 *
 * [1, 2, 3] --> [2, 4, 6]
 */

#include <stddef.h>
#include <stdlib.h>

int *maps(const int *arr, size_t arr_size) {
  int *result = malloc(arr_size * sizeof(int));
  if (result == NULL) {
    return NULL;
  }
  for (size_t i = 0; i < arr_size; i++) {
    result[i] = arr[i] * 2;
  }
  return result;
}
