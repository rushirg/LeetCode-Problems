"""
1389. Create Target Array in the Given Order
https://leetcode.com/problems/create-target-array-in-the-given-order/
"""


"""
Method 1: (Slow)
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [-1 for length in range(len(nums))]
        for i in range(len(nums)):
            n = nums[i]
            ind = index[i]
            if target[ind] != -1:
                target = target[:ind] + [n] + target[ind:]
                target.remove(-1)
            else:
                target[ind] = n
        return target


"""
Method 2: (Better)
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
