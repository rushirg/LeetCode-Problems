"""
524. Longest Word in Dictionary through Deleting

- https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/
"""

# Method 1

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""

