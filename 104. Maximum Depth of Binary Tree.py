# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1

         
MySolution = Solution()


root = [3,9,20,None,None,15,7]

print(MySolution.maxDepth(root))# True
# #########################################

root = [1,None,2]

print(MySolution.maxDepth(root))# false
# #########################################

# root = [1]

# print(MySolution.inorderTraversal(root))# [1]
# #########################################