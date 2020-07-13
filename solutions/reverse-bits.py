"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""

class Solution:
    def reverseBits(self, n: int) -> int:

        # convert integer to equivalent binary string and remove first 2 character 0b
        str_n = bin(n)[2:]

        # add any 0s by substracting 32 from the length of string
        str_n_32 = (32 - len(str_n)) * "0" + str_n

        # reverse the string and covert it to integer

        return int(str_n_32[::-1], 2)

