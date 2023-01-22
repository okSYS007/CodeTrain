class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return 1

test1 = 4
test2 = 8
# test3 = [49]

MySolution = Solution()
print(MySolution.mySqrt(test1))# 2 The square root of 4 is 2, so we return 2.
print(MySolution.mySqrt(test2))# 2 The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#print(MySolution.mySqrt(test3))# [1,0]
#print(MySolution.mergeTwoLists(test4))# False