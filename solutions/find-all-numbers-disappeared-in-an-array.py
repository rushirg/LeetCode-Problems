"""
448. Find All Numbers Disappeared in an Array
- https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/
"""

# Method 1
# Time: O(N)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
