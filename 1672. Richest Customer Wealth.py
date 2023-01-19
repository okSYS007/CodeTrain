class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0
        max = 0
        
        for x in accounts:
            for y in x:
                sum += y
            if sum > max:
                max = sum
            sum = 0

        return max


accounts1 = [[1,2,3],[3,2,1]] #6
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
accounts2 = [[1,5],[7,3],[3,5]] #10
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
accounts3 = [[2,8,7],[7,1,3],[1,9,5]] #17

MySolution = Solution()
print(MySolution.maximumWealth(accounts1))
print(MySolution.maximumWealth(accounts2))
print(MySolution.maximumWealth(accounts3))
