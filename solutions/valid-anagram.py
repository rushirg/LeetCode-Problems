"""
242. Valid Anagram
- https://leetcode.com/problems/valid-anagram/
"""


### Solution 1

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
