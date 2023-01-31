class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 1
        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
            else:
                s_result = s_result[s_result.index(i)+1:] + i

            if len(s_result) > count:
                count = len(s_result)
        
        return count

MySolution = Solution()

s = "abcabcbb"

print(MySolution.lengthOfLongestSubstring(s))# 3
# #########################################

s = "bbbbb"

print(MySolution.lengthOfLongestSubstring(s))# 1
# #########################################

s = "pwwkew"

print(MySolution.lengthOfLongestSubstring(s))# 3
# #########################################

