# The Millionth Fibonacci

| Field | Value |
|-------|-------|
| Slug | the-millionth-fibonacci |
| Kyu | 3 |
| Link | https://www.codewars.com/kata/53d40c1e2f13e331fc000c26 |
| Status | backfilled |
| Reference | languages/python/3kyu/the-millionth-fibonacci.py |

## Summary

Compute F(n) exactly for very large |n| (e.g. n = 1,000,000). Use fast doubling for O(log n) big-integer arithmetic. Sequence: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). For negative n: F(-n) = (-1)^(n+1) · F(n).

## Input / Output

- **Input:** Integer `n` (may be negative or very large).
- **Output:** Exact integer F(n).
- **Constraints:** Must handle indices far beyond 64-bit range; no floating point.

## Examples

| Input | Output |
|-------|--------|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 10 | 55 |
| -5 | 5 |
| 1,000,000 | (very large integer) |

## Edge Cases

- n = 0 → 0 immediately.
- Negative n: sign = -1 if n is even (for -n positive), else +1; multiply F(|n|).
- n = 1 → 1 without full bit scan if optimized.

## Approach

- **Algorithm:** Iterative fast doubling — maintain (F(k), F(k+1)); for each bit of n from MSB to LSB, apply doubling identities then optionally advance k→k+1.
- **Time:** O(log n) multiplications on big integers
- **Space:** O(1) aside from big-int size

## Behavioral Contract

- Identities: F(2k) = F(k)·(2·F(k+1) − F(k)); F(2k+1) = F(k)² + F(k+1)².
- After doubling step, if current bit of n is 1: (F(m), F(m+1)) ← (F(2m+1), F(2m)+F(2m+1)).
- Negative extension: F(-k) = (-1)^(k+1) × F(k) for k > 0.

## Pseudocode

```text
FUNCTION fib(n):
  IF n == 0: RETURN 0
  IF n < 0:
    k = -n
    sign = -1 IF k IS EVEN ELSE 1
    RETURN sign * fibPositive(k)
  RETURN fibPositive(n)

FUNCTION fibPositive(n):
  fib_m = 0          // F(m)
  fib_m1 = 1         // F(m+1)
  FOR bit FROM MSB(n) DOWN TO 0:
    fib_2m   = fib_m * (2*fib_m1 - fib_m)
    fib_2m1  = fib_m*fib_m + fib_m1*fib_m1
    IF bit i of n is 1:
      fib_m  = fib_2m1
      fib_m1 = fib_2m + fib_2m1
    ELSE:
      fib_m  = fib_2m
      fib_m1 = fib_2m1
  RETURN fib_m
```

## Walkthrough

For n = 5 (binary `101`):

1. Start (F(0), F(1)) = (0, 1).
2. Process bits MSB→LSB; after handling `101`, state yields F(5) = **5**.

For n = -5: F(5)=5, sign (-1)^(5+1)=+1 → **5**.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Python | `fib(n)` | Fast doubling, big ints |
