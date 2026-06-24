/**
 * Title: Array plus array
 * Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).
 */

public class Sum {

  public static int arrayPlusArray(int[] arr1, int[] arr2) {
    int sum = 0;
    for (int n : arr1) {
      sum += n;
    }
    for (int n : arr2) {
      sum += n;
    }
    return sum;
  }

}
