"""
Title: Tortoise racing
Link: https://www.codewars.com/kata/55e2adece53b4cdcb900006c
Difficulty: 6 kyu

## Description

Tortoise A has speed v1 and tortoise B has speed v2 (feet per hour). When B starts, A has a lead of
g feet. How long until B catches A? Return [hour, min, sec] with whole seconds (floor). If v1 >= v2,
B never catches A — return None.
"""


def race(v1, v2, g):
    if v1 >= v2:
        return None
    total_seconds = g * 3600 // (v2 - v1)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return [h, m, s]
