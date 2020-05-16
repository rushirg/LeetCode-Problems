"""
1394. Find Lucky Integer in an Array
https://leetcode.com/problems/find-lucky-integer-in-an-array/submissions/
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        myDict = {}
        for num in arr:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        lucky = []
        for k in myDict:
            if myDict[k] == k:
                lucky.append(k)
        if len(lucky):
            return max(lucky)
        return -1
