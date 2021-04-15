"""
509. Fibonacci Number
- https://leetcode.com/problems/fibonacci-number/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3709/
"""

# Method 1
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n == 0:
            return a
        elif n == 1 or n == 2:
            return b
        result = 0
        a = 1
        while n >= 3:
            result = a + b
            a = b
            b = result
            n -= 1
        return result
