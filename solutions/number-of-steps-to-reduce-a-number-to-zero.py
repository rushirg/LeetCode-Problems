"""
1342. Number of Steps to Reduce a Number to Zero
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while(num > 0):
            if num % 2 == 0:
                num /= 2
                count += 1
                continue
            else:
                num = num - 1
                count += 1
        return count
