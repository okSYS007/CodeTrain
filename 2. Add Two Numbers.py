
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.next is None:
            return l1.next
        else:
            root = self.addTwoNumbers(l1.next, l2)
        
        return root

from time import perf_counter

MyClass = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
# l1 = [2,4,3]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(MyClass.addTwoNumbers(l1, l2)) #[7,0,8]  342 + 465 = 807.

# l1 = [0]
# l2 = [0]
# print(MyClass.addTwoNumbers(l1, l2)) # [0]

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# print(MyClass.addTwoNumbers(l1, l2)) # [8,9,9,9,0,0,0,1]


# start = perf_counter()
# print(MyClass.addTwoNumbers(l1, l2))
# print(f"time: {(perf_counter() - start):.02f}")

# start = perf_counter()
# print(MyClass.addTwoNumbers(l1, l2))
# print(f"time: {(perf_counter() - start):.02f}")

