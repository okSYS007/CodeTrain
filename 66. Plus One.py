class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last = digits[-1]
        if last == 9:
            if len(digits) == 1:
                return [1,0]
            return self.plusOne(digits[:-1]) + [0]
        digits[-1] += 1
        return digits

test1 = [1,2,3]
test2 = [4,3,2,1]
test3 = [49]

MySolution = Solution()
print(MySolution.plusOne(test1))# [1,2,4]
print(MySolution.plusOne(test2))# [4,3,2,2]
print(MySolution.plusOne(test3))# [1,0]
#print(MySolution.mergeTwoLists(test4))# False
