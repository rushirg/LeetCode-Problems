"""
1752. Check if Array Is Sorted and Rotated

- https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
- https://leetcode.com/contest/weekly-contest-227/problems/check-if-array-is-sorted-and-rotated/
"""

# Method 1

class Solution:
    def check(self, nums: List[int]) -> bool:
      # sort the list
	  numsSorted = sorted(nums)

	  # iterate over all list elements
	  for i in range(len(nums)):
		  # check every rotate option with the sorted list
		  # if found return True
		  if nums[i:] + nums[:i] == numsSorted:
			  return True
	  return False

