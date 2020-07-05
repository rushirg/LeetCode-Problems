"""
1385. Find the Distance Value Between Two Arrays
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
"""


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            found = False
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    found = True
                    break
            if not found:
                count += 1
        return(count)