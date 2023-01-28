class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            if(i == 0):
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                # Calculate for each of the next values...
                while(j < i):
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j-1] + prev[j])
                    j+=1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output       # Return 

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