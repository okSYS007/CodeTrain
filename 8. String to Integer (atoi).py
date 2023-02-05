class Solution(object):
    def myAtoi(self, x):
        """
        :type x: int
        :rtype: int
        """
        return 1


MySolution = Solution()

x = "42"

print(MySolution.myAtoi(x))# 42
# #########################################

x = "   -42"

print(MySolution.myAtoi(x))# -42
# #########################################

x = "4193 with words"

print(MySolution.myAtoi(x))# 4193
# # #########################################

# x = [1,2]

# print(MySolution.myAtoi(x))# 2.50000
# # #########################################
