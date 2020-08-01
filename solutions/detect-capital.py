"""
520. Detect Capital
https://leetcode.com/problems/detect-capital/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # base case
        if len(word) is 1: return True

        # check for invalid use of capitals
        # if first character is lowercase and second character is uppercase
        if word[0] >= "a" and word[1] < "a":
            return False

        # set flag to check for characters from 3 and onwards
        if (word[0] >= "a" and word[1] >= "a") or (word[0] >= "A" and word[1] >= "a"):
            # for first and second small characters and
            # for first upper and second lower case character
            flag = "small"
        elif word[0] >= "A" and word[1] >= "A":
            # for first and second uppercase character
            flag = "caps"

        # iterate over remaining characters
        for i in range(2, len(word)):
            # for flag set to caps and if character is lower case and
            # for flag set to small and if character is upper case
            if (flag == "caps" and word[i] >= "a") or (flag == "small" and word[i] <= "Z"):
                return False

        # otherwise valid use of capitals
        return True


