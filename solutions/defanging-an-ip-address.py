"""
Solution for problem 1108
https://leetcode.com/problems/defanging-an-ip-address/
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')



