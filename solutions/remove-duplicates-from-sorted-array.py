"""
26. Remove Duplicates from Sorted Array
- https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3258/
"""

# Method 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: count += 1
            else:
                nums[i - count] = nums[i]
        return len(nums) - count


# Similar to above but using two pointer method
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j];
        return i + 1
