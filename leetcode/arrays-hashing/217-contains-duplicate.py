#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

problem = Solution()
print(problem.containsDuplicate([1,2,3,1]))