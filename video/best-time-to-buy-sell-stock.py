# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         res = 0
#         l = 0

#         for r in range(l, len(prices)):
#             if prices[l] < prices[r]:
#                 l = r
#             res = max(res, prices[r] - prices[l])
#         return res


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res



sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))