// Title: Array plus array
// Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
// Difficulty: 8 kyu
//
// ## Description
//
// Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).

fn slice_plus_slice(arr1: &[i32], arr2: &[i32]) -> i32 {
    arr1.iter().chain(arr2.iter()).sum()
}
