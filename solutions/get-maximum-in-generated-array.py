"""
1646. Get Maximum in Generated Array
https://leetcode.com/problems/get-maximum-in-generated-array/
https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/
"""


# Method 1
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        maxNum = 1
        for i in range(1, n + 1):
            if (2 * i) <= n:
                nums[2 * i] = nums[i]
                maxNum = max(nums[2 * i], maxNum)
            if (2 * i) + 1 <= n:
                nums[(2 * i) + 1] = nums[i] + nums[i + 1]
                maxNum = max(nums[(2 * i) + 1], maxNum)
        return maxNum

