
# Definition for singly-linked list.
#sum of 2 listnodes
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list_from_ListNode(l1):
    list1 = []
    while l1: #is not None
        list1.append(l1.val)
        l1 = l1.next
    return list1

def make_ListNode_from_list(a_list):
    head = l3 = ListNode(a_list[0])
    for x in a_list[1:]:
        l3.next = l3 = ListNode(x)
    return head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       
        list1 = make_list_from_ListNode(l1)
        list2 = make_list_from_ListNode(l2)

        ### RIGHT PAD WITH ZEROES
        len_list1 = len(list1)
        len_list2 = len(list2)
        if len_list1 > len_list2:
            pad = len_list1 - len_list2
            list2 = list2 + [0,] * pad
        elif len_list2 > len_list1:
            pad = len_list2 - len_list1
            list1 = list1 + [0,] * pad

        ### DO THE MATH
        d = 0
        the_sum = list()
        for x,y in zip(list1, list2):
            d, m = divmod(x + y + d, 10)
            the_sum.append(m)
        if d != 0:
            the_sum.append(d)
        return make_ListNode_from_list(the_sum)

MyClass = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(MyClass.addTwoNumbers(l1, l2)) 
