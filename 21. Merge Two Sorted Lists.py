# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return True

test1 = [1,2,4] 
list1 = [1,3,4]

test2 = []
list2 = []

test3 = []
list3 = [0]



MySolution = Solution()
print(MySolution.mergeTwoLists(test1, list1))# [1,1,2,3,4,4]
print(MySolution.mergeTwoLists(test2, list2))# []
print(MySolution.mergeTwoLists(test3, list3))# [0]
#print(MySolution.mergeTwoLists(test4))# False
