-- Title: Array plus array
-- Link: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
-- Difficulty: 8 kyu
--
-- ## Description
--
-- Return the sum of every element in two integer arrays (i.e. sum of the first array plus sum of the second).

function array_plus_array(arr1, arr2)
  local sum = 0
  for i = 1, #arr1 do
    sum = sum + arr1[i]
  end
  for i = 1, #arr2 do
    sum = sum + arr2[i]
  end
  return sum
end

return array_plus_array
