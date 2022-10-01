# 49. GROUP ANAGRAMS
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# pseudo
# result = map (defaultdict)
# FOR s in strings
  # count = [0] * 26
  # FOR c in s
    # count[ord(c) - ord("a")] += 1
  # result[tuple(count)].append(s)
# return ans.values()


# class Solution(object):
#   def groupAnagrams(self, strs):
#     """
#     :type strs: List[str]
#     :rtype: List[List[str]]
#     """
#     result = defaultdict(list)

#     for s in strs:
#       count = [0] * 26
#       for c in s:
#         count[ord(c) - ord("a")] += 1
#       result[tuple(count)].append(s)
#     return result.values()
    

class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = defaultdict(list)
    for str in strs:
      s = ''.join(sorted(str))
      dic[s].append(str)

    return dic.values()

# time : O(m * n)