# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

list1 = ListNode([1,2,4])
list2 = ListNode([1,3,4])

list3 = ListNode([])
list4 = ListNode([])

list5 = ListNode([])
list6 = ListNode([0])

MySolution = Solution()
print(MySolution.mergeTwoLists(list1, list2))# [1,1,2,3,4,4]
print(MySolution.mergeTwoLists(list3, list4))# []
print(MySolution.mergeTwoLists(list5, list6))# [0]
#print(MySolution.mergeTwoLists(test4))# False
