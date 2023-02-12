class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxx = 0 
        i = 0
        j = len(height)-1
        while i < j:
            width = abs(i-j)
            area = width * min(height[i],height[j])
            maxx = max(area,maxx)
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return maxx 

MySolution = Solution()

height = [1,8,6,2,5,4,8,3,7]


print(MySolution.maxArea(height))# 49
# #########################################

height = [1,1]

print(MySolution.maxArea(height))# -42
# #########################################

height = [1,8,6,2,5,4,8,3,7]

print(MySolution.maxArea(height))# 4193
# # #########################################

# x = [1,2]

# print(MySolution.maxArea(height))# 2.50000
# # #########################################
