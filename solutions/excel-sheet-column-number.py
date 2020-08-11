"""
171. Excel Sheet Column Number
- https://leetcode.com/problems/excel-sheet-column-number/
- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        sLen = len(s)
        for i in range(len(s)):
            result += (26**(sLen-1)) * (ord(s[i]) - ord('A') + 1)
            sLen -= 1
        return(result)
