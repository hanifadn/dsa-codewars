"""
Title: Pete, the baker
Link: https://www.codewars.com/kata/525c65e51bf619685c000059
Difficulty: 5 kyu

## Description

Given a recipe dict (ingredient -> amount needed per cake) and available amounts, return how many
whole cakes you can bake. Missing ingredients count as 0.
"""


def cakes(recipe, available):
    limits = []
    for ingredient, need in recipe.items():
        if need == 0:
            continue
        have = available.get(ingredient, 0)
        limits.append(have // need)
    return min(limits) if limits else 0
