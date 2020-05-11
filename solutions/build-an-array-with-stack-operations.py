"""
1441. Build an Array With Stack Operations
https://leetcode.com/problems/build-an-array-with-stack-operations/
https://leetcode.com/contest/weekly-contest-188/problems/build-an-array-with-stack-operations/
"""


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        count = 1
        while count <= target[-1]:
            if count in target:
                result.append("Push")
                count += 1
            else:
                result.append("Push")
                result.append("Pop")
                count += 1
        return result
