"""
- 118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""

# Method 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        for i in range(2, numRows + 1):
            temp = [0 for j in range(i)]
            for j in range(len(temp)):
                if j == 0:
                    temp[j] = result[-1][0]
                elif j == len(temp) - 1:
                    temp[j] = result[-1][-1]
                elif j != 0 and j != len(temp) - 1:
                    newNum = result[-1][j-1] + result[-1][j]
                    temp[j] = (newNum)
            result.append(temp)
        return result
