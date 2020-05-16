"""
1380. Lucky Numbers in a Matrix
https://leetcode.com/problems/lucky-numbers-in-a-matrix/
"""


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # iterate rows to get min
        minSet = set()
        for i in range(len(matrix)):
            minSet.add(min(matrix[i]))

        # iterate on columns to get max
        maxSet = set()
        for i in range(len(matrix[0])):
            maxVal = 0
            for j in range(len(matrix)):
                if matrix[j][i] > maxVal:
                    maxVal = matrix[j][i]
            maxSet.add(maxVal)
        return list(minSet.intersection(maxSet))
