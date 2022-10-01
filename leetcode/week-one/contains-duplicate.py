# 217. CONTAINS DUPLICATE
# # notebook no. 2

# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# pseudo
# use SET and 
# FOR n in nums
  # if n in SET return TRUE
  # add n to SET
# (return false)

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
      if n in hashset:
        return True
      hashset.add(n)
    return False