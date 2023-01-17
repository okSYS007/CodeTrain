class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False


ransomNote1 = "a" 
magazine1 = "b"

ransomNote2 = "aa" 
magazine2 = "ab"

ransomNote3 = "aa" 
magazine3 = "aab"

MySolution = Solution()
print(MySolution.canConstruct(ransomNote1, magazine1))
print(MySolution.canConstruct(ransomNote2, magazine2))
print(MySolution.canConstruct(ransomNote3, magazine3))