class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        matrix = {
            "firstRow": 1,
            "secRowLeft": 1, "secRowRight" : 1,
            "thirdRowLeft": 1, "thirdRowCenter": 0, "thirdRowRight": 1,
            "fourthRowLeft": 1, "fourthRowCenterLeft": 0, "fourthRowCenterRight": 0, "fourthRowRight": 1,
            "fifthRowLeft": 1, "fifthRowCenterLeft": 0, "fifthRowCenter": 0, "fifthRowCenterRight": 0, "fifthRowRight": 1,
            }

        for x in range(numRows):
            pass

        return 1


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