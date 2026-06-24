-- Title: Beginner - Lost Without a Map
-- Link: https://www.codewars.com/kata/57f781872e3d8ca2a000007e
-- Difficulty: 8 kyu
--
-- ## Description
--
-- Given an array of integers, return a new array with each value doubled.
--
-- ## Examples
--
-- [1, 2, 3] --> [2, 4, 6]

local solution = {}

function solution.maps(a)
  local result = {}
  for i = 1, #a do
    result[i] = a[i] * 2
  end
  return result
end

return solution
