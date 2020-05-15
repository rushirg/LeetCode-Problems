"""
1304. Find N Unique Integers Sum up to Zero
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        result = []
        for i in range(1, n//2 + 1):
            result.append(i)
            result.append(-i)
        if n % 2 != 0:
            result.append(0)
        return result