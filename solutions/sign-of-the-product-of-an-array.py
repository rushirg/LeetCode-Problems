"""
1822. Sign of the Product of an Array
- https://leetcode.com/problems/sign-of-the-product-of-an-array/
- https://leetcode.com/contest/weekly-contest-236/problems/sign-of-the-product-of-an-array/
"""

# Method 1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for x in nums:
            product *= x
        if product == 0:
            return product
        elif product > 0:
            return 1
        return -1


# slight variation in Method 1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for x in nums:
            if x == 0:
                return x
            elif x < 0:
                product = -product
        return product
