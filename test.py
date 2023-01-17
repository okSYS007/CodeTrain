#Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RomanDict = {
            "I": 1, 
            "V": 5,
            "X": 10, 
            "L": 50,
            "C": 100, 
            "D": 500,
            "M": 1000,
            }
        
        rez = 0
        for i in range(len(s)):
            if i + 1 < len(s) and RomanDict[s[i]] < RomanDict[s[i + 1]]:
                rez -= RomanDict[s[i]]
            else:
                rez += RomanDict[s[i]]

        return rez


MyClass = Solution()

test1 = "III"
test2 = 'LVIII'
test3 = 'MCMXCIV'
test = "IV"
print(MyClass.romanToInt(test))
print(MyClass.romanToInt(test1))
print(MyClass.romanToInt(test2))
print(MyClass.romanToInt(test3))