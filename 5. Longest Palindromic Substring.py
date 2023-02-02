class Solution:
    def longestPalindrome(self, s: str) -> str:

        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=len)
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

MySolution = Solution()

s = "babad"

print(MySolution.longestPalindrome(s))# "bab"
# #########################################

s = "cbbd"

print(MySolution.longestPalindrome(s))# "bb"
# #########################################

# nums1 = [1,3]
# nums2 = [2,7]

# print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# # #########################################

# nums1 = []
# nums2 = [1]

# print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# # #########################################

# nums1 = []
# nums2 = [2,3]

# print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# # #########################################

# nums1 = [3]
# nums2 = [-2,-1]

# print(MySolution.findMedianSortedArrays(nums1, nums2))# 2.50000
# # #########################################
