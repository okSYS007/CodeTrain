
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

        return 1

from time import perf_counter

MyClass = Solution()

l1 = [2,4,3]
l2 = [5,6,4]
print(MyClass.addTwoNumbers(l1, l2)) #[7,0,8]  342 + 465 = 807.

l1 = [0]
l2 = [0]
print(MyClass.addTwoNumbers(l1, l2)) # [0]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(MyClass.addTwoNumbers(l1, l2)) # [8,9,9,9,0,0,0,1]


# start = perf_counter()
# print(MyClass.addTwoNumbers(l1, l2))
# print(f"time: {(perf_counter() - start):.02f}")

# start = perf_counter()
# print(MyClass.addTwoNumbers(l1, l2))
# print(f"time: {(perf_counter() - start):.02f}")

