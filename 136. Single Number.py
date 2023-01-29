class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        rezNum = 0
        for num in nums:
            if num not in hashMap:
                hashMap.update({num:1})
            else:
                val = hashMap[num]
                hashMap.update({num:val+1})

        for key, value in hashMap.items():
            if value == 1:
                return key

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
