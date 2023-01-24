# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return 1

MySolution = Solution()


root = [1,None,2,3]

print(MySolution.inorderTraversal(root))# [1,3,2]
#########################################

root = []

print(MySolution.inorderTraversal(root))# []
#########################################

root = [1]

print(MySolution.inorderTraversal(root))# [1]
#########################################