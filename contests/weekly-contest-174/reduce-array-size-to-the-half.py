"""
1338. Reduce Array Size to The Half
https://leetcode.com/contest/weekly-contest-174/problems/reduce-array-size-to-the-half/
Credits: Alex Wice [https://leetcode.com/awice]
"""


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = sorted(Counter(arr).values())
        todo = (len(arr) + 1) // 2
        ans = 0

        while todo > 0:
            todo -= freq.pop()
            ans += 1
        return ans
