"""
1356. Sort Integers by The Number of 1 Bits
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda a: [bin(a).count('1'), a])

