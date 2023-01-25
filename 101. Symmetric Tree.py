# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True

        
MySolution = Solution()


root = [1,2,2,3,4,4,3]

print(MySolution.isSymmetric(root))# True
# #########################################

root = [1,2,2,null,3,null,3]

print(MySolution.isSymmetric(root))# false
# #########################################

# root = [1]

# print(MySolution.inorderTraversal(root))# [1]
# #########################################