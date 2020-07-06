"""
1399. Count Largest Group
https://leetcode.com/problems/count-largest-group/
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        myDict = {}
        for i in range(1, n + 1):
            digSum = sum(map(int, str(i)))
            if digSum in myDict:
                myDict[digSum].append(i)
            else:
                myDict[digSum] = [i]

        maxLen = max([len(x) for x in myDict.values()])

        count = 0
        for x in myDict:
            if len(myDict[x]) == maxLen:
                count += 1
        return count