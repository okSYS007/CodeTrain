# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return 1


MySolution = Solution()


nums = [-10,-3,0,5,9]

print(MySolution.sortedArrayToBST(nums))# [0,-3,9,-10,null,5]
# #########################################

nums = [1,3]

print(MySolution.sortedArrayToBST(nums))# [3,1]
# #########################################

# root = [1]

# print(MySolution.inorderTraversal(root))# [1]
# #########################################