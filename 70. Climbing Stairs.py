class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        d = [1, 2]
        for i in range(2, n):
            d.append(d[i-1] + d[i-2])
        return d[-1]

test1 = 2
test2 = 3
# test3 = [49]

MySolution = Solution()
print(MySolution.climbStairs(test1))# 2 
print(MySolution.climbStairs(test2))# 3
#print(MySolution.mySqrt(test3))# [1,0]
#print(MySolution.mergeTwoLists(test4))# False