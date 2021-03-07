"""
1785. Minimum Elements to Add to Form a Given Sum
- https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
- https://leetcode.com/contest/weekly-contest-231/problems/minimum-elements-to-add-to-form-a-given-sum/
"""

# Method 1
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        def isLess(n):
            if n == 0:
                return 0
            if n // limit == 0:
                return 1
            tmp = n // limit
            tmp2 = n % limit
            return tmp + isLess(tmp2)

        totalSum = sum(nums)
        x = goal - totalSum
        return isLess(abs(x))
