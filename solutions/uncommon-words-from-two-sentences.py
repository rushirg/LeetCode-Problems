"""
884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""

### Solution 1
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        self.myDict = {}
        def buildDict(d):
            for w in d.split():
                if w in self.myDict:
                    self.myDict[w] += 1
                else:
                    self.myDict[w] = 1
        buildDict(A)
        buildDict(B)
        result = []
        for k, v in self.myDict.items():
            if v == 1:
                result.append(k)
        return result


### Solution 2
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        myCounter = Counter( (A + " " + B).split())
        for k, v in myCounter.items():
            if v == 1: result.append(k)
        return result
