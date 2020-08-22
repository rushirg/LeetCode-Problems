"""
905. Sort Array By Parity
- https://leetcode.com/problems/sort-array-by-parity/
- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        oddList = []
        evenList = []
        for x in A:
            if x % 2 == 0:
                evenList.append(x)
            else:
                oddList.append(x)
        return evenList + oddList
