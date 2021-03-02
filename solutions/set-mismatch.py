"""
645. Set Mismatch
- https://leetcode.com/problems/set-mismatch/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/
"""

# Method 1

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        totalSum = len(nums) * (len(nums) + 1)// 2
        myDict = {}
        res = []
        for x in nums:
            if x in myDict:
                res.append(x)
                missingNum = totalSum - (sum(nums) - x)
                res.append(missingNum)
                break
            myDict[x] = 1
        return res



# Method 2

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        myDict = {}
        for x in nums:
            if x in myDict:
                res.append(x)
                break
            myDict[x] = 1

        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
                break

        return res
