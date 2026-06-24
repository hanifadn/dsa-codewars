"""
Title: The Millionth Fibonacci
Link: https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
Difficulty: 3 kyu

## Description

Compute F(n) exactly for very large n (e.g. the millionth Fibonacci). Use an O(log n) method (fast doubling).
The sequence satisfies F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). For negative indices,
F(-n) = (-1)^(n+1) F(n) for n > 0.
"""


def fib(n):
    if n == 0:
        return 0
    if n < 0:
        positive_index = -n
        return _fib_negation_sign(positive_index) * _fib_positive(positive_index)
    return _fib_positive(n)


def _fib_negation_sign(positive_index):
    """Multiplier for F(-k): F(-k) = sign * F(k), sign = (-1)^(k+1)."""
    return -1 if positive_index % 2 == 0 else 1


def _fib_positive(n):
    """
    F(n) for n >= 1 via iterative fast doubling (MSB→LSB over bits of n).

    Uses F(2k) = F(k) * (2*F(k+1) - F(k)) and F(2k+1) = F(k)^2 + F(k+1)^2,
    maintaining a pair (F(m), F(m+1)) while scanning bits of n.
    """
    fib_m, fib_m_plus_1 = 0, 1
    for bit_index in range(n.bit_length() - 1, -1, -1):
        fib_2m = fib_m * (2 * fib_m_plus_1 - fib_m)
        fib_2m_plus_1 = fib_m * fib_m + fib_m_plus_1 * fib_m_plus_1
        if (n >> bit_index) & 1:
            fib_m, fib_m_plus_1 = fib_2m_plus_1, fib_2m + fib_2m_plus_1
        else:
            fib_m, fib_m_plus_1 = fib_2m, fib_2m_plus_1
    return fib_m
