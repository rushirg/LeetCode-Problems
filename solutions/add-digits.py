"""
258. Add Digits
https://leetcode.com/problems/add-digits/
"""
class Solution:
    def addDigits(self, num: int) -> int:

        # to solve this problem in O(1)
        # there is property of numbers
        # if the number is divided by 9 then its sum of digits is also divided by 9

        # base case
        if num is 0:
            return 0

        # if num is divided by 9 return 9
        if num % 9 == 0:
            return 9

        # for all other numbers
        else:
            return num % 9
