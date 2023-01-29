class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True


MySolution = Solution()

s = "A man, a plan, a canal: Panama"

print(MySolution.isPalindrome(s))# 5 "amanaplanacanalpanama" is a palindrome.
# #########################################

s = "race a car"

print(MySolution.isPalindrome(s))# "raceacar" is not a palindrome.
# #########################################

s = " "

print(MySolution.isPalindrome(s))# s is an empty string "" after removing non-alphanumeric characters.
# #########################################