"""
1556. Thousand Separator
- https://leetcode.com/contest/biweekly-contest-33/problems/thousand-separator/
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        count = 0
        result = ""
        for i in range(len(n_str) - 1, -1, -1):
            if count == 3:
                result += "."
                count = 0
            count += 1
            result += n_str[i]
        return result[::-1]
