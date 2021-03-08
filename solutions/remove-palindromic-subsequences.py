"""
1332. Remove Palindromic Subsequences
- https://leetcode.com/problems/remove-palindromic-subsequences/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/
"""

# Method 1
# Time: O(N)
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPallin(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        # check if empty string, if found return 0 
        if len(s) == 0:
            return 0
        # check for pallindrom, if found return 1
        if isPallin(s):
            return 1
        # otherwise return 2, as it only has 2 letters
        return 2

# Method 2
# Time: O(N)
# Short version of Method 1

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        elif s == s[::-1]:
            return 1
        return 2


# even shorter
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
