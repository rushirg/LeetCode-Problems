"""
1539. Kth Missing Positive Number
biweekly-contest-32
- https://leetcode.com/problems/kth-missing-positive-number/
- https://leetcode.com/contest/biweekly-contest-32/problems/kth-missing-positive-number/
"""

# Solution 1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missCount = 0
        i = 1
        missNum = 0
        while missCount < k:
            if i not in arr:
                missCount += 1
                missNum = i
            i += 1
        return missNum
