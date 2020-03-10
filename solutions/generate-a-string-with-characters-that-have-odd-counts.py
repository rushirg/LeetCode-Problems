"""
1374. Generate a String With Characters That Have Odd Counts
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""
class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        elif n == 0:
            return ""
        elif n % 2 == 0:
            # even case
            return 'a'*(n-1)+'b'
        elif n % 2 == 1:
            # odd case
            return 'a'*(n-2)+'b'+'c'
        else:
            return ""
