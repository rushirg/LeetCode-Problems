"""
724. Find Pivot Index

- https://leetcode.com/problems/find-pivot-index/
"""

# Method 1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # calculate sum of elements
	total = sum(nums)
	
        # intialize leftsum to 0
        leftSum = 0
	
        # initialize rightsum to sum of list(total)
        rightSum = total
	# initialize result index to -1
        
        index = -1

        for i in range(len(nums)):
            # subtract element from rightsum
	    rightSum -= nums[i]
	    # check if rightsum is equal to leftsum
	    # if yes, update the result index to the current index and break from loop
	    # else, continue to the next element from the list
            if rightSum == leftSum:
                index = i
                break
	    # add the element to the leftSum
            leftSum += nums[i]
        return index
