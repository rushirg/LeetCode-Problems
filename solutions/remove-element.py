"""
27. Remove Element
https://leetcode.com/problems/remove-element/submissions/
"""


# Solution 1:
# remove all the elements from nums 
class Solution:
    def removeVal(self, i, nums):
        for i in range(i, len(nums) - 1):
            nums[i] = nums[i + 1]
        del nums[len(nums)-1]

    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                self.removeVal(i, nums)
                i = 0
            else:
                length += 1
                i += 1
        return length

# Solution 2:
# logically removing values from nums
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
