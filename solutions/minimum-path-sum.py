"""
64. Minimum Path Sum
- https://leetcode.com/problems/minimum-path-sum/
"""

# Method 1
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        for i in range(1, col):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])

        return grid[row-1][col-1]
