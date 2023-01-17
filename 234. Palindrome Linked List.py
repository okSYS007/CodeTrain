# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return True


test1 = [1,2]
test2 = [1,2,2,1]

MySolution = Solution()
print(MySolution.isPalindrome(test1))
print(MySolution.isPalindrome(test2))