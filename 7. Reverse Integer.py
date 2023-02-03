class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x * -1)[::-1]) * -1
        
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        
        if ans > ma or ans < mi:
            return 0
        return ans
        
MySolution = Solution()

x = 123

print(MySolution.reverse(x))# 321
# #########################################

x = -123

print(MySolution.reverse(x))# -321
# #########################################

x = 120

print(MySolution.reverse(x))# 21
# # #########################################

x = 901000

print(MySolution.reverse(x))# 2.50000
# #########################################
