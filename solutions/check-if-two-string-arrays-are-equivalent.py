"""
Problem Statement: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Contest: https://leetcode.com/contest/weekly-contest-216/problems/check-if-two-string-arrays-are-equivalent/

Weekly Contest 216: https://leetcode.com/contest/weekly-contest-216/
"""

# Method 1

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # this is pretty easy one
        # I'll define two empty strings to combine two strings from list
        word1list, word2list = '', ''

        # now iterate over two list and combine the words in it respectively
        for x in word1: word1list += x
        for y in word2: word2list += y

        # in word1list and word2list we have combine all the words in both the lists now we will compare them or we will return the result from
        # their comparision

        return word1list == word2list



# Method 2

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # we can easily do this program in one line, using python list join method
        
        # we will join the words from each list and directly compare them, without any loop 
        
        return "".join(word1) == "".join(word2)

