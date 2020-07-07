"""
66. Plus One
https://leetcode.com/problems/plus-one/
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newNum = int("".join(map(str, digits))) + 1
        return [x for x in str(newNum)]