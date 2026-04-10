"""
Title: Sum Arrays
Link: https://www.codewars.com/kata/53dc54212259ed3d4f00071c
Difficulty: 8 kyu

## Description

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.

## Examples

```text
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: [-2.398]
Output: -2.398

Input: []
Output: 0
```

## Details

- **Assumptions**: You can assume that you are given a (possibly empty) valid array containing only numbers.
- **Goal**: We're testing basic loops and math operations.
"""

def sum_array(a):
    return sum(a)