"""
775. Global and Local Inversions
- https://leetcode.com/problems/global-and-local-inversions/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3697/
"""

# Solution 1
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        val = A[0]
        for i in range(2, len(A)):
            if val > A[i]:
                return False
            val = max(val, A[i-1])
        return True


# Solution 2
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
