"""
Title: Binary Addition
Link: https://www.codewars.com/kata/551f37452ff852b7bd000139
Difficulty: 7 kyu

## Description

Add two integers and return their sum as a binary string (no `0b` prefix).

## Examples

- `1, 1` → `"10"` (1 + 1 = 2 → `10` in binary)
- `5, 9` → `"1110"` (5 + 9 = 14 → `1110` in binary)
"""


def add_binary(a: int, b: int) -> str:
    return bin(a + b)[2:]
