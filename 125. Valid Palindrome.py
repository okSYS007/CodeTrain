class Solution(object):

    def isPalindrome(self, s):
        import re
        """
        :type s: str
        :rtype: bool
        """
        myStr = re.sub(":|,|\s", "", s).lower()
        if myStr == myStr[::-1]:
            return True
        else:
            return False


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