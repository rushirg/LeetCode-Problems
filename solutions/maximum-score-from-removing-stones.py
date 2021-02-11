"""
1753. Maximum Score From Removing Stones

- https://leetcode.com/problems/maximum-score-from-removing-stones/
- https://leetcode.com/contest/weekly-contest-227/problems/maximum-score-from-removing-stones/
"""

# Method 1
# Math

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # either all 3 can become zero in that case (a+b+c)//2
        # or 2 can become zero, which is sum - max
        # the minimum of these two is our result
        return min((a + b + c) // 2, a + b + c - max(a, b, c))


# Method 2
# Sort
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # sort the three numbers
        tmp = sorted([a,b,c])
        res = 0
        # loop unitil last two numbers becomes zero
        # after removing one element sort the array again to remove from last two big numbers
        while tmp[1] and tmp[2]:
            tmp[1] -= 1
            tmp[2] -= 1
            res += 1
            tmp.sort()
        return res



# Method 3
# Sort + Math
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # sort the number
        tmp = sorted([a,b,c])
        # after sorting if first two numbers are less than the last, return their sum
        if tmp[0] + tmp[1] < tmp[2]:
            return tmp[0] + tmp[1]
        # otherwise all sum//2 which means all 3 becomes 0
        return (a + b + c) // 2
