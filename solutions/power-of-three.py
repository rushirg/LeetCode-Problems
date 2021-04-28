"""
326. Power of Three
- https://leetcode.com/problems/power-of-three/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722/
"""

# Method 1
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 or n == 2:
            return False
        while n:
            if n == 1:
                break
            if n % 3 != 0:
                return False
            n = n // 3
        return True
