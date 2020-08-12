"""
119. Pascal's Triangle II
- https://leetcode.com/problems/pascals-triangle-ii/
- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex == 0:
            return result
        if rowIndex == 1:
            result.append(1)
            return result
        if rowIndex == 2:
            result.insert(1, 2)
            result.append(1)
            return result

        result = [1, 2, 1]

        for k in range(3, rowIndex + 1):
            temp = [1]
            for i in range(len(result) - 1):
                temp.append(result[i] + result[i + 1])
            temp.append(1)
            result = temp
        return result
