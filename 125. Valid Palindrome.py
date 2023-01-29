class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filter = ''.join([i.lower() for i in s if i.isalnum()])
        return filter == filter[::-1]


MySolution = Solution()

s = "A man, a plan, a canal: Panama"

print(MySolution.isPalindrome(s))# true
# #########################################

s = "race a car"

print(MySolution.isPalindrome(s))# false
# #########################################

s = "A man, a plan, a canal -- Panama"

print(MySolution.isPalindrome(s))# true
# #########################################

s = "Marge, let's \"[went].\" I await {news} telegram."
print(MySolution.isPalindrome(s))# true
# #########################################
