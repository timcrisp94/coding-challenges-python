class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      maxf = l = 0
      count = collections.Counter()

      for r in range(len(s)):
        count[s[r]] += 1
        maxf = max(maxf, count[s[r]])
        if r - l + 1 > maxf + k:
          count[s[l]] -= 1
          l += 1
      return len(s) - l