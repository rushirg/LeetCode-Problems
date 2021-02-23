"""
240. Search a 2D Matrix II
- https://leetcode.com/problems/search-a-2d-matrix-ii/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/
"""


# Method 1
# O(M+N)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        col, row = len(matrix[0]) - 1, 0
        while col >=0 and row <= len(matrix) - 1:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False


# Method 2
# O(MxN)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == target:
                    return True
        return False
