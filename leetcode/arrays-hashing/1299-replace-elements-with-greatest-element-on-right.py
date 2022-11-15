"""
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

                    
17 | 18 | 5 | 4 | 6 | 1 | | -1  

iterate thrrough array backwards checking for the max value
# initial max = -1
# new max = max(old max, arr[i])
"""

class Solution(object):
    def replaceElements(self, arr):
        """
        type arr: List[int]
        rtype: List[int]
        """
        rightMax = -1

        # iterate reverse order without making shallow copy
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr

problem = Solution()
print(problem.replaceElements([17,18,5,4,6,1]))


