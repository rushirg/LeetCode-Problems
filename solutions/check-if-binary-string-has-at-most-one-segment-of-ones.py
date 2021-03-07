"""
1784. Check if Binary String Has at Most One Segment of Ones
- https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
- https://leetcode.com/contest/weekly-contest-231/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
"""

# Method 1
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        res = []
        count = 0
        for ch in s:
            if ch == "1":
                count += 1
            else:
                if count != 0: res.append(count)
                count = 0

        if count != 0: res.append(count)
        return len(res) == 1
