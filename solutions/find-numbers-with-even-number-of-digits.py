"""
1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

# Method 1a - fast 36ms
# (Converting int to str)
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count


# Method 1b - slow 44ms:
# (Converting int to str)
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count


# Method 2:
# (Using log10 from math module)
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        count = 0
        for i in range(len(nums)):
            if  (int(math.log10(nums[i])) + 1) % 2 == 0:
                count += 1
        return count
