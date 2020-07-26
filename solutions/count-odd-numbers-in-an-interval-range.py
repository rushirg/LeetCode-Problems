"""
1523. Count Odd Numbers in an Interval Range

 - https://leetcode.com/contest/biweekly-contest-31/problems/count-odd-numbers-in-an-interval-range/

 - https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""

# Solution 1:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # another way to solve this problem is
        # we can calculate the difference between these numbers
        count = (high - low) // 2

        # if either one of them is odd we increment the counter
        if high % 2 != 0 or low % 2 != 0:
            count += 1

        # return the count
        return count


# Solution 2:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # we can find the odd number from 0...high and subtract those from 0...low
        # i.e. for f(x) = f(x + 1) // 2
        
        return (high + 1) // 2 - low // 2
        
