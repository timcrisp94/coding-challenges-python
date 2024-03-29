# 53 - Maximum Subarray

# Given an integer array nums, 
# find the contiguous subarray 
# (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# pseudo
# *greedy algorithm*
# max = nums[0]
# cur = 0
# for n in nums
  # edge case: if cur < 0: cur = 0
  # cur += n
  # max(max, cur)
# return max

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = 0
        maxSum = nums[0]

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxSum = max(maxSum, cur)
        return maxSum
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))