# 33/11. SEARCH IN SORTED ARRAY
# * binary search *

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, 
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity. 
# * note: they are all but saying "use a binary search" with this

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# pseudo
# n = nums.len
# l = 0
# r = n - 1
# WHILE l <= r
  # mid = (l+r) // 2
  # IF target = nums[mid] return mid
  # (search left sorted portion)
  # IF nums[l] <= nums[mid]
    # IF target > nums[mid] or target < nums[l]
      # l = mid + 1
    # ELSE:
      # r = mid - 1
  # (search right sorted portion)
  # ELSE:
    # IF target < nums[mid] or target > nums[r]
      # r = mid - 1
    # ELSE:
      # l = mid + 1
# return -1 

class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l <= r:
      mid = (l + r)

      if target == nums[mid]:
        return mid
      
      if nums[l] <= nums[mid]:
        if target > nums[mid] or target < nums[l]:
          l = mid + 1
        else:
          r = mid - 1

      else:
        if target < nums[mid] or target > nums[r]:
          r = mid - 1
        else:
          l = mid + 1
    return -1

