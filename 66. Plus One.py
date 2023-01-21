class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return 2

test1 = [1,2,3]
test2 = [4,3,2,1]
test3 = [9]

MySolution = Solution()
print(MySolution.plusOne(test1))# [1,2,4]
print(MySolution.plusOne(test2))# [4,3,2,2]
print(MySolution.plusOne(test3))# [1,0]
#print(MySolution.mergeTwoLists(test4))# False
