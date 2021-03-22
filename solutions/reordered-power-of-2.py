"""
869. Reordered Power of 2
- https://leetcode.com/problems/reordered-power-of-2/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/
"""

# Method 1
# counting total digits with 2 power digits
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = collections.Counter(str(N))
        for x in range(31):
            if collections.Counter(str(1 << x)) == count:
                return True
        return False




# Method 2
# sorting digits and comparing with sorted 2 power digits
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        count = sorted([int(x) for x in str(N)])
        for x in range(31):
            if sorted([int(n) for n in str(1 << x)]) == count:
                return True
        return False

