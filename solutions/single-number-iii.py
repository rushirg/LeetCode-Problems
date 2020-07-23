"""
260. Single Number III
https://leetcode.com/problems/single-number-iii/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        myDict = {}
        for x in nums:
            if x in myDict:
                del myDict[x]
            else:
                myDict[x] = 1
        return list(myDict.keys())
