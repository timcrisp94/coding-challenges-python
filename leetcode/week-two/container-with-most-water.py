# 11/14. CONTAINER WITH THE MOST WATER

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# ex: input = [1,8,6,2,5,4,8,3,7], out = 49

# - pseudo - 
# * two pointers
# const n = height.length
# l = 0
# r = len(height) - 1
# res = 0
# WHILE l < r
#   res = max(res, min(height[l], height[r]) * (r - 1))
#   IF height[l] < height[r]
#     l += 1
#   ELIF height[r] <= height[l]:
#     l++


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res
