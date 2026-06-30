# Grasshopper - Debug

| Field | Value |
|-------|-------|
| Slug | grasshopper-debug |
| Kyu | 8 |
| Link | https://www.codewars.com/kata/55cb854deb36f11f130000e1 |
| Status | backfilled |
| Reference | languages/python/8kyu/grasshopper-debug.py |

## Summary

Convert a Fahrenheit temperature to Celsius using `celsius = (fahrenheit - 32) * (5/9)`, then return a descriptive string. If the Celsius value is less than or equal to zero, report freezing; otherwise report above freezing. The original kata had a bug using integer division for `5/9`; use floating-point division.

## Input / Output

- **Input:** A numeric temperature in Fahrenheit (`temp`).
- **Output:** A string of the form `"{celsius} is freezing temperature"` or `"{celsius} is above freezing temperature"`.
- **Constraints:** Use floating-point arithmetic for the conversion; compare the computed Celsius value against zero.

## Examples

| Input (°F) | Celsius | Output |
|------------|---------|--------|
| `32` | `0.0` | `"0.0 is freezing temperature"` |
| `50` | `10.0` | `"10.0 is above freezing temperature"` |
| `23` | `-5.0` | `"-5.0 is freezing temperature"` |

## Edge Cases

- Exactly `32` °F → `0` °C → freezing message.
- Values producing Celsius `<= 0` → freezing branch.
- Use `5/9` as floating-point division, not integer division (the bug to fix).

## Approach

- **Algorithm:** Compute Celsius with float arithmetic, branch on `celsius <= 0`, format the Celsius value into the required string template.
- **Time:** O(1).
- **Space:** O(1).

## Behavioral Contract

- Conversion formula: `celsius = (fahrenheit - 32) * (5 / 9)` with real/float division.
- Freezing when `celsius <= 0` (inclusive).
- String templates: `"{celsius} is freezing temperature"` or `"{celsius} is above freezing temperature"`.
- Python/JavaScript references embed the float Celsius value directly in the string. Groovy truncates toward zero to `int` before comparison and formatting.

## Pseudocode

```text
FUNCTION weather_info(temp):
  celsius = (temp - 32) * (5 / 9)    // floating-point division
  IF celsius <= 0:
    RETURN FORMAT("{celsius} is freezing temperature", celsius)
  ELSE:
    RETURN FORMAT("{celsius} is above freezing temperature", celsius)
```

## Walkthrough

For `temp = 50`:

1. `celsius = (50 - 32) * (5 / 9) = 18 * 0.555… = 10.0`.
2. `10.0 <= 0` is false.
3. Return `"10.0 is above freezing temperature"`.

For `temp = 23`:

1. `celsius = (23 - 32) * (5 / 9) = -9 * 0.555… = -5.0`.
2. `-5.0 <= 0` is true.
3. Return `"-5.0 is freezing temperature"`.

## Codewars

| Language | Entry point | Notes |
|----------|-------------|-------|
| Groovy | `static String weatherInfo(double temp)` | Truncates Celsius to `int` toward zero before compare/format |
| JavaScript | `function weatherInfo(temp)` | Float division; embeds float in template string |
| Python | `def weather_info(temp)` | Float division; f-string with float value |
