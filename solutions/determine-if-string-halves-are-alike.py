"""
1704. Determine if String Halves Are Alike
- https://leetcode.com/problems/determine-if-string-halves-are-alike/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3699/
"""

# Method 1
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        strlen = len(s) // 2
        a = s[:strlen]
        b = s[strlen:]
        aCounter = collections.Counter(a)
        bCounter = collections.Counter(b)
        vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        aCount = bCount = 0
        for ch in vowelsList:
            if ch in aCounter:
                aCount += aCounter[ch]
            if ch in bCounter:
                bCount += bCounter[ch]
        return aCount == bCount
