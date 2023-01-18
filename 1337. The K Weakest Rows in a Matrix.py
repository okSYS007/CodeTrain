class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        return 1


mat1 =  [[1,1,0,0,0], #[2,0,3]
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]], 
k1 = 3

mat2 = [[1,0,0,0], #[0,2]
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]], 
k2 = 2

MySolution = Solution()

print(MySolution.kWeakestRows(mat1, k1))
print(MySolution.kWeakestRows(mat2, k2))
