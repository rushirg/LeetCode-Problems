"""
377. Combination Sum IV
- https://leetcode.com/problems/combination-sum-iv/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3713/ 
"""

# Method 1
# using DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                if (i - n) >= 0:
                    dp[i] += dp[i-n]
        return dp[target]
