class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        return nums1

MySolution = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(MySolution.merge(nums1, m, nums2, n))# [1,2,2,3,5,6]
#####

nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(MySolution.merge(nums1, m, nums2, n))# [0]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(MySolution.merge(nums1, m, nums2, n))# [1,2,2,3,5,6]
#The arrays we are merging are [1,2,3] and [2,5,6].
#The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1 = [1]
m = 1
nums2 = []
n = 0

print(MySolution.merge(nums1, m, nums2, n))# [1]

# The arrays we are merging are [1] and [].
# The result of the merge is [1].

nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(MySolution.merge(nums1, m, nums2, n))# [1]

# The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


