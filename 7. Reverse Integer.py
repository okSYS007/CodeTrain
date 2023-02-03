class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        return -int(str(x)[::-1].replace("-", "").replace("0", "")) if x < 0 else int(str(x)[::-1].replace("-", "").replace("0", ""))
        
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
