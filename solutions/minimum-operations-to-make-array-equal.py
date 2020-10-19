"""
1551. Minimum Operations to Make Array Equal
- https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"""

### Solution 1

class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i) + 1 for i in range(n)]
        target = sum(arr) // n
        tmp = arr[:len(arr) // 2]
        count = 0
        for c in tmp:
            count += target - c
        return count


### Solution 2

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            n //= 2
            return n * (n + 1)
        else:
            n //= 2
            return n * n
