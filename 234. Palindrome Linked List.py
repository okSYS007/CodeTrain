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
        def check(head):
            if (head == None):
                return True
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res;
        
        self.temp = head
        return check(head);
       

#ListNode

# test1 = [1,2]
# test2 = [1,2,2,1]

# MySolution = Solution()
# print(MySolution.isPalindrome(test1))
# print(MySolution.isPalindrome(test2))