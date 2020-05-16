"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


"""
Method 1: (Using Counter)
"""
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        myNums = Counter(nums)
        result = []
        for n in myNums:
            if myNums[n] == 2:
                result.append(n)
        return result

