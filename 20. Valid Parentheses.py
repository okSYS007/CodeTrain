class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charSym = {
            "(":")",
            "{": "}",
            "[":"]"
        }
        rez = True
        for sym in s:
            if sym in charSym.values():
                continue
            if charSym[sym] in s:
                rez = True
            else:
                rez = False
            
        return rez


test1 = "()"
test2 = "()[]{}"
test3 = "(]"


MySolution = Solution()
print(MySolution.isValid(test1))# True
print(MySolution.isValid(test2))# True
print(MySolution.isValid(test3))# False
