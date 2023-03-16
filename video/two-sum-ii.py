# Given a *1-indexed* array of integers numbers that is already *sorted* in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# PSEUDOCODE
# -two pointers-
# l,r = 0, N-1
# WHILE l < r
#   sum = nums[l] + nums[r]
#   IF sum < target
#       l--
#   ELIF sum > target
#       r++
#   ELSE 
#       return [l+1,r+1]


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
            
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))