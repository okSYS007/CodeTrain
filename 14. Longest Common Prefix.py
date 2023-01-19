class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short = min(strs, key=len) # short = "flow"
        for item in strs: # When item = "flight"
            while len(short) > 0:
                if item.startswith(short): # during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                    break
                else:
                    short = short[:-1] # during loop 1 short = flo, during loop 2 short = fl
        return short


strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["flower","flow","floght"]


MySolution = Solution()
print(MySolution.longestCommonPrefix(strs1))#"fl"
print(MySolution.longestCommonPrefix(strs2))# "" There is no common prefix among the input strings.
print(MySolution.longestCommonPrefix(strs3))# "" There is no common prefix among the input strings.
