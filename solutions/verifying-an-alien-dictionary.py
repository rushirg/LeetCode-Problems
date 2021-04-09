"""
953. Verifying an Alien Dictionary
- https://leetcode.com/problems/verifying-an-alien-dictionary/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3702/
"""

# Method 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordIndexSum = []
        for word in words:
            wordSum = []
            for ch in word:
                wordSum.append(order.index(ch))
            wordIndexSum.append(wordSum)

        return wordIndexSum == sorted(wordIndexSum)
