class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #find min value + index
        minPrice = prices[0]
        maxPrice = 0
        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            elif price > maxPrice:
                maxPrice = price

        #find max value from min value +index
        return maxPrice - minPrice if maxPrice > 0 else 0

MySolution = Solution()

prices = [7,1,5,3,6,4]

print(MySolution.maxProfit(prices))# 5 Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# #########################################

prices = [7,6,4,3,1]

print(MySolution.maxProfit(prices))# 0
# #########################################

# root = [1]

# print(MySolution.inorderTraversal(root))# [1]
# #########################################