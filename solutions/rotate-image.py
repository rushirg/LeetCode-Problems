"""
48. Rotate Image
- https://leetcode.com/problems/rotate-image/
"""

# Method 1
# Transpose and then reverse each row

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # reverse each row
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

