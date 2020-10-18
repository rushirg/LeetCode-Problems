"""
970. Powerful Integers
- https://leetcode.com/problems/powerful-integers/submissions/
"""


### Solution 1

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(20):
            if (x ** i + y ** 0) > bound:
                break
            for j in range(20):
                tmp = x ** i + y ** j
                if tmp > bound:
                    break
                result.add(tmp)
        return list(result)
