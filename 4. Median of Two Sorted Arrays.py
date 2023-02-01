class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        rezNum = []

        for num in nums1:
            rezNum.append(num)
        
        for num in nums2:
            rezNum.append(num)

        x = sum(rezNum) / len(rezNum)

        return x
    

MySolution = Solution()

nums1 = [1,3]
nums2 = [2]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.000000
# #########################################

nums1 = [1,2]
nums2 = [3,4]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################

# s = "pwwkew"

# print(MySolution.findMedianSortedArrays(s))# 3
# # #########################################

