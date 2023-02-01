class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1+nums2)
        l = len(num)
        return num[int(l/2)] if l % 2 != 0 else (num[int(l/2)] + num[int((l/2))-1]) / 2
        # if l%2!=0:
        #     return num[int(l/2)]
        # else:
        #     return (num[int(l/2)] + num[int((l/2))-1])/2
        


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



