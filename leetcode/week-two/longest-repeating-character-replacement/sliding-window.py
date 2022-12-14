# 424/16. LONGEST REPEATING CHAR REPLACEMENT

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# - PSEUDO - 
# * sliding window *
# n = s.len
# hash = {}
# left, right, max = 0
# WHILE r < n
#   hash[s[right]] = hash[s[right]] OR 0 + 1
#   max = max(max, hash[s[right]])
#   IF right - left + 1 - max > k
#     hash[s[left]]--
#     left += 1
#   right += 1
# return right - left

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
          count[s[r]] = 1 + count.get(s[r], 0)
          maxf = max(maxf, count[s[r]])

          if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

          res = max(res, r - l + 1)
        return res