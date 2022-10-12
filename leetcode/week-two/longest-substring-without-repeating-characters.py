# 3/17. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# * sliding window *

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# - pseudo - 
# sub = set()
# l, r, m = 0, 0, 0
# WHILE r < len(s):
  # WHILE s[r] in sub:
    # sub.remove(s[l])
    # l += 1
  # sub.add(s[r])
  # m = max(m, r - 1 + 1)
  # r += 1
# return m

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = set()
        j, l, m = 0, 0, 0

        while j < len(s):
            while s[j] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[j])
            m = max(m, j - l + 1)
            j += 1
        return m
