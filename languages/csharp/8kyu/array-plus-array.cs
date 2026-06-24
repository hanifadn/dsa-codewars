/**
 * Title: Array plus array
 * Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
 * Difficulty: 8 kyu
 *
 * ## Description
 *
 * Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).
 */

using System.Linq;

public static class Kata
{
    public static int ArrayPlusArray(int[] arr1, int[] arr2) =>
        arr1.Sum() + arr2.Sum();
}
