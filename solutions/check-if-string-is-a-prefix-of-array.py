"""
1961. Check If String Is a Prefix of Array

- https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
- https://leetcode.com/contest/weekly-contest-253/problems/check-if-string-is-a-prefix-of-array/
"""

# Method 1
# O(N)
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        for word in words:
            res += word
            if res == s:
                return True
        return False
