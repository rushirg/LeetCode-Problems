"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
https://leetcode.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for c in candies:
            if (maxCandies - c) <= extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
