"""
Solution for Problem 557
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(w[::-1] for w in s.split(" "))

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])[::-1]

"""

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(" ")
        le = len(l)
        ans = ""
        for i in range(le-1):
            ans = ans + l[i][::-1] + " "
        ans += s.split(" ")[le-1][::-1]
        return ans
"""
