"""
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
"""


### Solution 1

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        myDict = Counter(text)
        count = 0
        while True:
            if 'b' not in myDict or 'a' not in myDict or 'l' not in myDict or 'o' not in myDict or 'n' not in myDict:
                break
            if myDict['b'] < 1 or myDict['a'] < 1 or myDict['l'] < 2 or myDict['o'] < 2 or myDict['n'] < 1:
                break
            myDict['b'] -= 1
            myDict['a'] -= 1
            myDict['l'] -= 2
            myDict['o'] -= 2
            myDict['n'] -= 1
            count += 1
        return count


### Solution 2

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])
