class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True


test1 = "()"
test2 = "()[]{}"
test3 = "(]"


MySolution = Solution()
print(MySolution.isValid(test1))# True
print(MySolution.isValid(test2))# True
print(MySolution.isValid(test3))# False
