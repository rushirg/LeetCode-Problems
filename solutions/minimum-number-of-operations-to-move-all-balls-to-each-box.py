"""
1769. Minimum Number of Operations to Move All Balls to Each Box
- https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""

# Method 1
# Time: O(N^2)
# Space: O(N)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # create a list to store the index of "1"
        setIndex = []
        # iterate over boxes and store the index of "1" in the list
        for i in range(len(boxes)):
            if boxes[i] == "1":
                setIndex.append(i)
        # define restult list
        res = []
        # iterate over boxes
        for i in range(len(boxes)):
            # set total steps to 0
            total = 0
            # iterate over setIndexes of "1" and take absolute sum with all setIndexes
            for x in setIndex:
                total += abs(i - x)
            # append the result to result list
            res.append(total)
        return res


# Method 2
# Time: O(N)
# Space: O(N)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0 for x in range(len(boxes))]
        ops = cnt = 0
        for i in range(len(boxes)):
            res[i] += ops
            if boxes[i] == "1":
                cnt += 1
            ops += cnt

        ops = cnt = 0
        for i in range(len(boxes) - 1, -1, -1):
            res[i] += ops
            if boxes[i] == "1":
                cnt += 1
            ops += cnt

        return res

