# 647/29. PALINDROMIC SUBSTRINGS

# given a string s, return the number of palindromic substrings in it

# -palindrome
# -substring

# example 1:
# input: s = "abc"
# output: 3
# "a", "b", "c"

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for i in range(len(s)):
          res += self.countPali(s, i, i)
          res += self.countPali(s, i, i + 1)
        return res
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
          res += 1
          l-= 1
          r += 1
        return res        