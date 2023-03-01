# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        return 1
    

nums1 = [2,11,7,15]

nums2 = [3,2,4]

nums3 = [3,2,4]

nums4 = [4,5,2]


MySolution = Solution()
print(MySolution.getIntersectionNode(nums1))#[0,1] Because nums[0] + nums[1] == 9, we return [0, 1].
print(MySolution.getIntersectionNode(nums2))#[1,2]
print(MySolution.getIntersectionNode(nums3))#[0,1]
print(MySolution.getIntersectionNode(nums4))#[0,2]



