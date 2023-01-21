class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rez = []
        sum = ""
        for num in digits:
           sum += "".join(str(num))

        sum = int(sum)+1
        for num in str(sum):
            rez.append(int(num))
        return rez

test1 = [1,2,3]
test2 = [4,3,2,1]
test3 = [9]

MySolution = Solution()
print(MySolution.plusOne(test1))# [1,2,4]
print(MySolution.plusOne(test2))# [4,3,2,2]
print(MySolution.plusOne(test3))# [1,0]
#print(MySolution.mergeTwoLists(test4))# False
