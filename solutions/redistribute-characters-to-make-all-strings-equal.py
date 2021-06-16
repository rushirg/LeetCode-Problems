"""
1897. Redistribute Characters to Make All Strings Equal
- https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
- https://leetcode.com/contest/weekly-contest-245/problems/redistribute-characters-to-make-all-strings-equal/
"""


# Method 1
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        wordLen = len(words)
        myDict = Counter()
        for word in words:
            myDict += Counter(word)
        for k, v in myDict.items():
            if v % wordLen != 0:
                return False
        return True
