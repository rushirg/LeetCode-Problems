"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        tempCount = 0
        for x in nums:
            if x is 1:
                tempCount += 1
            else:
                count = max(count, tempCount)
                tempCount = 0
        return max(count, tempCount)