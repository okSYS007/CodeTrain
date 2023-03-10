# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#List node

# head1 = [1,2,3,4,5]
# head2 = [1,2,3,4,5,6]

# MySolution = Solution()
# print(MySolution.middleNode(head1))
# print(MySolution.middleNode(head2))