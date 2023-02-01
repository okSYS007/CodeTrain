class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        rezNum = []

        rezNum = nums1 + nums2
        rezNum.sort()
        mid = len(rezNum) // 2

        return float(rezNum[mid]) if len(rezNum) == 1 or (mid % 2 != 0 and mid % 2 != 1) else (rezNum[:mid][len(rezNum[:mid])-1] + rezNum[mid::][-len(rezNum[:mid])]) / 2


MySolution = Solution()

nums1 = [1,3]
nums2 = [2]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.000000
# #########################################

nums1 = [1,2]
nums2 = [3,4]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################

nums1 = [1,3]
nums2 = [2,7]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################

nums1 = []
nums2 = [1]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################

nums1 = []
nums2 = [2,3]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################

nums1 = [3]
nums2 = [-2,-1]

print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# #########################################



