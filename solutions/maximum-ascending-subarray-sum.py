"""
1800. Maximum Ascending Subarray Sum
- https://leetcode.com/problems/maximum-ascending-subarray-sum/
- https://leetcode.com/contest/weekly-contest-233/problems/maximum-ascending-subarray-sum/
"""


# Method 1
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = tempMax = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                tempMax += nums[i]
            else:
                tempMax = nums[i]
            maxSum = max(maxSum, tempMax)
        return maxSum
