"""
120. Triangle
- https://leetcode.com/problems/triangle/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/
"""

# Method 1
# Time: O(N), modify triangle in-place

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] =  triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1] + triangle[i][j], triangle[i - 1][j] + triangle[i][j])
            print(triangle[i])
        return min(triangle[-1])



# Method 2
# Space: O(N) without modifying original triangle
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prevRow = triangle[0]
        for i in range(1, len(triangle)):
            currRow = []
            for j in range(len(triangle[i])):
                smallAbove = float('-inf')
                if j == 0:
                    smallAbove =  prevRow[j]
                elif j == len(triangle[i]) - 1:
                    smallAbove = prevRow[j - 1]
                else:
                    smallAbove = min(prevRow[j-1], prevRow[j])
                currRow.append(smallAbove + triangle[i][j])
            prevRow = currRow
        return min(prevRow)
