class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = sorted(set(nums))
        return len(nums)


test1 = [1,1,2]
test2 = [0,0,1,1,1,2,2,3,3,4]

MySolution = Solution()
print(MySolution.removeDuplicates(test1))# 2 [1,2,_]
print(MySolution.removeDuplicates(test2))# 5 [0,1,2,3,4,_,_,_,_,_]
#print(MySolution.mergeTwoLists(test3))# [0]
#print(MySolution.mergeTwoLists(test4))# False
