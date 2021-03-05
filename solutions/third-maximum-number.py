"""
414. Third Maximum Number
- https://leetcode.com/problems/third-maximum-number/
- https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3231/
"""

# Method 1
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]


# Method 2
# O(N)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = secondMax = thirdMax = None
        for x in nums:
            if x == firstMax or x == secondMax or x == thirdMax:
                continue
            if firstMax == None or x > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = x
            elif secondMax == None or x > secondMax:
                thirdMax = secondMax
                secondMax = x
            elif thirdMax == None or x > thirdMax:
                thirdMax = x
        return firstMax if thirdMax == None else thirdMax
