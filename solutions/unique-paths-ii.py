"""
63. Unique Paths II
- https://leetcode.com/problems/unique-paths-ii/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/
"""

# Method 1
# DP

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]

        for j in range(1, row):
            if obstacleGrid[j][0] == 1:
                obstacleGrid[j][0] = 0
            else:
                obstacleGrid[j][0] = obstacleGrid[j - 1][0]


        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[row - 1][col - 1]

