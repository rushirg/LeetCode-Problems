"""
Solution of problem 796
https://leetcode.com/problems/rotate-string/
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(101):
            if(A == B):
                return True
            elif(A == "" or B == ""):
                return False
            A = A[1::] + A[0]
        return False


