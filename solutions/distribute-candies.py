"""
575. Distribute Candies
https://leetcode.com/problems/distribute-candies/
"""


### Solution 1

from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candiesCounter = Counter(candies)
        count = len(candies) // 2
        result = 0

        while count != 0:
            for k, v in candiesCounter.items():
                if count == 0:
                    break
                if v is 0:
                    continue
                candiesCounter[k] -= 1
                result += 1
                count -= 1
            return result


### Solution 2

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies) // 2, len(set(candies)))



### Solution 3

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        from collections import Counter
        myCnt = Counter(candyType)
        n = len(candyType) // 2
        return min(n, len(myCnt.keys()))
