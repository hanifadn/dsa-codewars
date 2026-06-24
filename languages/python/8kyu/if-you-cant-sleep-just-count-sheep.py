"""
Title: If you can't sleep, just count sheeps!!
Link: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
Difficulty: 8 kyu

## Description

If you can't sleep, just count sheeps!!

**Task**:
Given a non-negative integer, `3` for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`. Input will always be valid, i.e. no negative integers.
"""

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))