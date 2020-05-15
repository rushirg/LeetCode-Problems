"""
1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""


"""
Method 1: (Slow)
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        result = []
        for i in range(len(arr) - 1):
            maxVal = max(arr[i + 1:])
            result.append(maxVal)
        result.append(-1)
        return result


"""
Method 2: (Better)
Iterate the list from right side while keeping the greatest
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1]
        if len(arr) == 1:
            return result
        maxVal = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            tmp = arr[i]
            if tmp > maxVal:
                result.append(maxVal)
                maxVal = tmp
            else:
                result.append(maxVal)
        result.reverse()
        return result