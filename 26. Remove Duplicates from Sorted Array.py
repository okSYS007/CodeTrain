class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashNums = {}
        rez = []
        numsToAdd = 0
        for num in nums:
            if num in hashNums:
                numsToAdd += 1
                continue
            else:
                hashNums.update({num:num})
            
            rez.append(num)
                
        rezForReturn = len(rez)

        for _ in range(numsToAdd):
            rez.append("_")
        
        return rezForReturn


test1 = [1,1,2]
test2 = [0,0,1,1,1,2,2,3,3,4]

MySolution = Solution()
print(MySolution.removeDuplicates(test1))# 2 [1,2,_]
print(MySolution.removeDuplicates(test2))# 5 [0,1,2,3,4,_,_,_,_,_]
#print(MySolution.mergeTwoLists(test3))# [0]
#print(MySolution.mergeTwoLists(test4))# False
