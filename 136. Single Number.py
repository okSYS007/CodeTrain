class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 1


MySolution = Solution()

nums = [2,2,1]

print(MySolution.singleNumber(nums))# 1
# #########################################

nums = [4,1,2,1,2]

print(MySolution.singleNumber(nums))# 4
# #########################################

nums = [1]

print(MySolution.singleNumber(nums))# 1
# #########################################

# s = "Marge, let's \"[went].\" I await {news} telegram."
# print(MySolution.singleNumber(nums))# true
# # #########################################
