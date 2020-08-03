"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/submissions/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # create a temporary variable to hold the string with only alphanumeric characters
        temp = ""

        # iterate over each character and only add alphanumeric characters to temp variable
        # but we also need to convert the input string to lower case to have uniformity
        for ch in s.lower():
            if (ch >= "a" and ch <= "z") or (ch >= "0" and ch <= "9"):
                temp += ch

        # compare the temp and its reverse and return if they match or not
        return temp == temp[::-1]


