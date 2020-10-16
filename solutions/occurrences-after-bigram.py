"""
1078. Occurrences After Bigram
https://leetcode.com/problems/occurrences-after-bigram/
"""

### Solution 1
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        myText = text.split()
        result = []
        FirstSet = SecondSet = False
        for word in myText:
            if FirstSet and SecondSet:
                result.append(word)
                FirstSet = SecondSet = False
            if word == first:
                FirstSet = True
                continue
            if word == second and FirstSet:
                SecondSet = True
            else:
                FirstSet = False
        return result



### Solution 2
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text = text.split()
        for i in range(2, len(text)):
            if text[i - 2] == first and text[i - 1] == second:
                result.append(text[i])
        return result
