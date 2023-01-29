class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1=set(nums)
        nums1=list(set1)
        nums2=nums1
        nums1.extend(nums2)
        for i in nums:
            nums1.remove(i)
        
        return nums1[0]

MySolution = Solution()

nums = [2,2,1]

print(MySolution.singleNumber(nums))# 1
# #########################################

nums = [4,1,2,1,1,2]

print(MySolution.singleNumber(nums))# 4
# #########################################

nums = [1]

print(MySolution.singleNumber(nums))# 1
# #########################################

# s = "Marge, let's \"[went].\" I await {news} telegram."
# print(MySolution.singleNumber(nums))# true
# # #########################################
