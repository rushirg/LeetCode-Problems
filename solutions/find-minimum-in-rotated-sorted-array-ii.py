"""
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

"""
The following are the three accepted solutions. The solutions 1 and 2 are not the best approach for this problem as the array/list is sorted and we can use this property.
But, I think the constraints are not strict for this problem so the solution 1 and 2 get accepted
"""

# Solution 1:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use the built-in min method
        return min(nums)

# Solution 2:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # by iterating over the list and comparing every number with min
        # and update if we found any min number than our initial min number
        # this is not correct way as the list is already sorted
        # but let's first try the worst way

        # initialize first number as min
        minNum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < minNum:
                minNum = nums[i]
        return minNum


# Solution 3:
class Solution:
    def findMin(self, nums: List[int]) -> int:

       # lets try with binary search as the aarray is sorted
        # yeah it is sorted but it is only pivoted
        # we can iterate and check

        # initialize left, right variables
        l = 0
        r = len(nums) - 1

        # loop until l is less than r
        while l < r:
            # get the mid index
            mid = l + (r - l) // 2

            # if the mid number is less than the rightmost number
            if nums[mid] < nums[r]:
                # it means that minimum element is in first half
                r = mid
            # if mid number is greater than right most number
            elif nums[mid] > nums[r]:
                # it means the array is pivoted in second half
                # the minimum number is in second half
                l = mid + 1

            # if mid and rightmost numbers are same then decrement the right counter
            else:
                r -= 1

        # return the number at l index
        return nums[l]

