"""
12. Integer to Roman
- https://leetcode.com/problems/integer-to-roman/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/
"""

# Method 1
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        myDict = {1000 : "M", 900: "CM", 500: "D", 400: "CD",
                  100: "C", 90: "XC", 50: "L", 40: "XL",
                  10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
                 }
        while num > 0:
            for n in myDict.keys():
                if num // n:
                    res += (num // n) * myDict[n]
                    num %= n

        return res
