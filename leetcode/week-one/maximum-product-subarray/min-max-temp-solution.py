# 152/10. Maximum Product Subarray
# * min, max, temp (kadane)

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# pseudo
# res = nums[0]
# max, min = 1
# FOR n in nums
  # temp = max * n
  # max = max(n * max, n * min, n)
  # min = (temp, n * min, n)
  # res = max(res, max)
# return res

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:
      temp = curMax * n
      curMax = max(n * curMax, n * curMin, n)
      curMin = min(temp, n * curMin, n)
      res = max(res, curMax)
    return res

# time/space = O(n)/O(1)