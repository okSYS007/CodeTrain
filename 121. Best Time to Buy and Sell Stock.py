class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        else:
            profit = 0
            minBuy = prices[0]
            for i in range(len(prices)):
                profit = max(prices[i] - minBuy, profit)
                minBuy = min(minBuy, prices[i])
            return profit

MySolution = Solution()

prices = [7,1,5,3,6,4]

print(MySolution.maxProfit(prices))# 5 Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# #########################################

prices = [7,6,4,3,1]

print(MySolution.maxProfit(prices))# 0
# #########################################

prices = [2,4,1]

print(MySolution.maxProfit(prices))# 2
# #########################################