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
        FirstL = True
        listForLoop = list1
        if len(list1) < len(list2):
            listForLoop = list2
            FirstL = False
       
        index = 0
        rez = []
        for x in range(len(listForLoop)):
            index += 1
            rez.append(listForLoop[x])
            if FirstL and len(list2) > 0: 
                rez.append(list2[x])
            elif not FirstL and len(list1) > 0:
                rez.append(list1[x])
        
        if len(list1) > len(list2):
            for num in list2[:index]:
                rez.append(num)
        elif len(list2) > len(list1):
            for num in list1[:index]:
                rez.append(num)

        return rez

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
