"""
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(len(nums)):
            count = 0
            for y in range(len(nums)):
                if(nums[y] < nums[x] and x != y):
                    count += 1
            ans.append(count)
        return ans


"""
Method 2
Faster 108ms using collections Counter

from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        for x in nums:
            cnt = 0
            for i in range(x):
                cnt += count[i]
            ans.append(cnt)
        return ans
"""
