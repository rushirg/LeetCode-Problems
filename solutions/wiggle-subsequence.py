"""
376. Wiggle Subsequence
- https://leetcode.com/problems/wiggle-subsequence/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3676/
"""

# Method 1
# Time: O(N)
# To do: Remove repetative comparisions 

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 0
        if nums[1] - nums[0] > 0:
            wiggle = "Positive"
        elif nums[1] - nums[0] < 0:
            wiggle = "Negative"
        else:
            wiggle = None

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 0: continue
            if wiggle == None:
                if diff > 0:
                    wiggle = "Positive"
                else:
                    wiggle = "Negative"

            if diff > 0 and wiggle == "Positive":
                count += 1
                wiggle = "Negative"
            elif diff < 0 and wiggle == "Negative":
                count += 1
                wiggle = "Positive"
        return count + 1



