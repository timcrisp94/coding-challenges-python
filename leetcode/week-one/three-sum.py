# 15. 3SUM
# # notebook no. 7

# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# pseudo

# res = []
# nums.sort
# FOR i, a in nums
  # IF i > 0 and a == nums[i-1] cont
  # l, r = i + 1 and len-1
  # WHILE l < r
    # three = a + nums[l] + nums[r]
    # IF three > 0 r -= 1
    # ELIF three < 0 l += 1
    # ELSE 
      # res.append([a, nums[l], nums[r]])
      # l += 1
      # WHILE nums[l] == nums[l-1] and l < r
        # l += 1



class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    for i, a in enumerate(nums):
      if i > 0 and a == nums[i-1]:
        continue

      l, r = i+1, len(nums) - 1
      while l < r:
        threeSum = a + nums[l] + nums[r]
        if threeSum > 0:
          r -= 1
        elif threeSum < 0:
          l += 1
        else:
          res.append([a, nums[l], nums[r]])
          l += 1
          while nums[l] == nums[l-1] and l < r:
            l += 1
    return res

# time : O(n2)