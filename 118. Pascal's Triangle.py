class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        newRow = self.generate(numRows - 1)
        newRow.append([1] * numRows)
        for i in range(1, numRows - 1):
            newRow[numRows - 1][i] = newRow[numRows - 2][i] + newRow[numRows - 2][i - 1]
        return newRow

MySolution = Solution()

numRows = 5

print(MySolution.generate(numRows))# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# #########################################

numRows = 1

print(MySolution.generate(numRows))# [[1]]
# #########################################

# root = [1]

# print(MySolution.inorderTraversal(root))# [1]
# #########################################