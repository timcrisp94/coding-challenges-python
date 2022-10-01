# 242. VALID ANAGRAM
# # notebook no. 4

# Given two strings s and t, 
# return true if t is an anagram of s, 
# and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# - pseudo - 
# function(s, t)
# hash = {}
# edge - if s.len !== t.len 
# for char of s
#   add to hash
# for char of t
#   if !hash[char]

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    countS, countT = {}, {}
    for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
