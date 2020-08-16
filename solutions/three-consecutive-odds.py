"""
1550. Three Consecutive Odds
- https://leetcode.com/problems/three-consecutive-odds/
- https://leetcode.com/contest/weekly-contest-202/problems/three-consecutive-odds/
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for x  in arr:
            if x % 2 != 0:
                oddCount += 1
            else:
                oddCount = 0
            if oddCount == 3:
                return True
        return False
