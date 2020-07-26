"""
1089. Duplicate Zeros
https://leetcode.com/problems/duplicate-zeros/
"""

# Solution 1:
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # let's find the index of zero value in the array
        zeroIndex = []
        arrLen = len(arr)
        for i in range(arrLen):
            if arr[i] == 0:
                zeroIndex.append(i)

        # if we didn't find 0 in the array return original array
        if len(zeroIndex) == 0:
            return arr

        # as we shift the index of zero, we will also move the later zero index
        secondIteration = 0

        for n in zeroIndex:
            if secondIteration:
                n += secondIteration
            for i in range(arrLen - 2, n-1, -1):
                arr[i + 1] = arr[i]
            secondIteration += 1


