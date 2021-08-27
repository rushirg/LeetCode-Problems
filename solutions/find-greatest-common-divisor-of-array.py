"""
1979. Find Greatest Common Divisor of Array

- https://leetcode.com/contest/weekly-contest-255/problems/find-greatest-common-divisor-of-array/
"""

# Method 1
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def getGCD(a, b):
            if a == 0: return b
            if b == 0: return a
            if a == b: return a
            if a > b: 
                return getGCD(a - b, b)
            return getGCD(a, b - a)
            
        maxNum = max(nums)
        minNum = min(nums)
        return getGCD(minNum, maxNum)
        
