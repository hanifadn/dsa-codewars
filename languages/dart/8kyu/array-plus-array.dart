/// Title: Array plus array
/// Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
/// Difficulty: 8 kyu
///
/// ## Description
///
/// Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).

int arrayPlusArray(List<int> arr1, List<int> arr2) {
  return [...arr1, ...arr2].fold(0, (sum, n) => sum + n);
}
