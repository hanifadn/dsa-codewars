"""
Title: The Hashtag Generator
Link: https://www.codewars.com/kata/52449b062fb80683ec000024
Difficulty: 5 kyu

## Description

Return a hashtag string: starts with `#`, each word title-cased and concatenated without spaces.
Return False if the input is empty/whitespace-only, or the result is longer than 140 characters.
"""


def generate_hashtag(s):
    words = s.split()
    if not words:
        return False
    tag = "#" + "".join(w[0].upper() + w[1:].lower() for w in words)
    return False if len(tag) > 140 else tag
