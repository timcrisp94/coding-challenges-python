# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Input: text = "nlaebolko"
# Output: 1

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        letters = ['b', 'a', 'l', 'o', 'n']
        counts = [0] * 5

        for i in range(5):
            counts[i] = text.count(letters[i])

        for i in range(2,4):
            counts[i] = counts[i] // 2

        return min(counts)


problem = Solution()
print(problem.maxNumberOfBalloons("loonbalxballpoon"))

        