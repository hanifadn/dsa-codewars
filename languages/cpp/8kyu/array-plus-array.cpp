/**
 * Title: Array plus array
 * Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).
 */

#include <numeric>
#include <vector>

int arrayPlusArray(std::vector<int> arr1, std::vector<int> arr2) {
  return std::accumulate(arr1.begin(), arr1.end(), 0) +
         std::accumulate(arr2.begin(), arr2.end(), 0);
}
