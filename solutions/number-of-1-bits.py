"""
Number of 1 Bits
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/
- https://leetcode.com/problems/number-of-1-bits/
"""

# Method 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # check until the number becomes zero
        while n != 0:
            # if number is divisible by 2 and reminder is 1 then increment count
            if n % 2: count += 1
            # update the number with the divisor
            n = int(n / 2)
        return count
            

# Method 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            # perform bitwise AND operation with number-1 to check the 
            # last bit is set(1) or not(0) if it is increment and update n
            n &= (n - 1)
        return count
