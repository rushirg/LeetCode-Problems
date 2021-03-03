"""
268. Missing Number
- https://leetcode.com/problems/missing-number/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/
"""

# Method 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsLen = len(nums)
        totalSum = numsLen * (numsLen + 1) // 2
        return totalSum - sum(nums)



