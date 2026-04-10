"""
Title: Invert Values
Link: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
Difficulty: 8 kyu

Description:
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
You can assume that all values are integers. Do not mutate the input array.
"""

def invert(lst):
    return [-num for num in lst]