# Array plus array

| Field | Value |
|-------|-------|
| Slug | array-plus-array |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/5a2be17aee1aaefe2a000151 |
| Status | backfilled |
| Reference | languages/python/8kyu/array-plus-array.py |

## Summary

Given two integer arrays, return the total sum of every element across both arrays. Concatenate the elements conceptually and add them together; order does not affect the result.

## Input / Output

- **Input:** Two arrays of integers (`arr1`, `arr2`). Either array may be empty.
- **Output:** A single integer — the sum of all elements in both arrays.
- **Constraints:** Elements are integers; result may exceed 32-bit range in some languages.

## Examples

| Input | Output |
|-------|--------|
| `[1, 2, 3]`, `[4, 5, 6]` | `21` |
| `[]`, `[1, 2, 3]` | `6` |
| `[1, 2, 3]`, `[]` | `6` |
| `[]`, `[]` | `0` |

## Edge Cases

- Both arrays empty → `0`.
- One array empty → sum of the non-empty array.
- Negative values are included in the total.
- Large magnitudes may require wider integer types (e.g. 64-bit).

## Approach

- **Algorithm:** Iterate over both arrays and accumulate each element into a running total (or concatenate then sum).
- **Time:** O(n + m), where n and m are the lengths of the two arrays.
- **Space:** O(1) extra space if summing in place; O(n + m) if materializing a combined collection first.

## Behavioral Contract

- Empty input arrays contribute `0` to the sum.
- Do not mutate caller-owned input arrays.
- Element order within each array does not affect the result.

## Pseudocode

```text
FUNCTION array_plus_array(arr1, arr2):
  total = 0
  FOR EACH value IN arr1:
    total = total + value
  FOR EACH value IN arr2:
    total = total + value
  RETURN total
```

## Walkthrough

For `arr1 = [1, 2, 3]` and `arr2 = [4, 5, 6]`:

1. Sum `arr1`: `1 + 2 + 3 = 6`.
2. Sum `arr2`: `4 + 5 + 6 = 15`.
3. Return `6 + 15 = 21`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| C | `long long arr_plus_arr(const int a[], const int b[], size_t na, size_t nb)` | Sums both arrays with explicit lengths |
| C# | `arrayPlusArray(int[] arr1, int[] arr2)` | LINQ sum over concatenated arrays |
| C++ | `int arrayPlusArray(std::vector<int> arr1, std::vector<int> arr2)` | Sums elements of both vectors |
| Dart | `int arrayPlusArray(List<int> arr1, List<int> arr2)` | Fold both lists into one total |
| Java | `public static int arrayPlusArray(int[] arr1, int[] arr2)` | Sum all elements of both arrays |
| JavaScript | `function arrayPlusArray(arr1, arr2)` | Concatenate then reduce |
| Lua | `function array_plus_array(arr1, arr2)` | Nested loops over both tables |
| Python | `def array_plus_array(arr1, arr2)` | `sum(arr1 + arr2)` |
| Ruby | `def array_plus_array(arr1, arr2)` | Sum of concatenated arrays |
| Rust | `fn slice_plus_slice(arr1: &[i32], arr2: &[i32]) -> i32` | Chain iterators and sum |
| Scala | `def arrayPlusArray(xs: Seq[Int], ys: Seq[Int]): Int` | Sum both sequences |
| TypeScript | `export function arrayPlusArray(arr1: number[], arr2: number[]): number` | Typed JS-style sum |
