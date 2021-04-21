"""
136. Single Number
- https://leetcode.com/problems/single-number/
"""

# Method 1
# Using XOR
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        for i in range(1, len(nums)):
            temp ^= nums[i]
        return temp


# Method 2
# XOR without extra memory but modifying existing list
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] ^ nums[i-1]
        return nums[len(nums) - 1]
