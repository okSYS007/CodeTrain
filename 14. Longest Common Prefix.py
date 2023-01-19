class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return True


strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]


MySolution = Solution()
print(MySolution.longestCommonPrefix(strs1))#"fl"
print(MySolution.longestCommonPrefix(strs2))# "" There is no common prefix among the input strings.
