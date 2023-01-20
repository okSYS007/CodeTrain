class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        charSym = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        lfind = []
        for sym in s:
            if sym in charSym.values():
                lfind.append(sym)
            elif lfind and charSym[sym] == lfind[-1]:
                lfind.pop()
            else:
                return False
            
        return lfind == []


test1 = "()"
test2 = "()[]{}"
test3 = "(]"
test4 = "([)]"


MySolution = Solution()
print(MySolution.isValid(test1))# True
print(MySolution.isValid(test2))# True
print(MySolution.isValid(test3))# False
print(MySolution.isValid(test4))# False
