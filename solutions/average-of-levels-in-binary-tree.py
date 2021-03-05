"""
637. Average of Levels in Binary Tree
- https://leetcode.com/problems/average-of-levels-in-binary-tree/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/
"""

# Method 1
# using BFS

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        myList = [root]
        while myList:
            tmp = 0
            myList2 = []
            for x in myList:
                tmp += x.val
                if x.left: myList2.append(x.left)
                if x.right: myList2.append(x.right)
            res.append(tmp / len(myList))
            myList = myList2

        return res


# Method 2
# using DFS

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        def average(node, i, res, count):
            if node == None: return
            if len(res) > i:
                res[i] = res[i] + node.val
                count[i] += 1
            else:
                res[i] = node.val
                count[i] = 1
            average(node.left, i + 1, res, count)
            average(node.right, i + 1, res, count)

        count = {}
        res = {}
        average(root, 0, res, count)
        result = []
        for i in range(len(res)):
            result.append(res[i] / count[i])
        return result


# Method 3
# Concise DFS
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        myList = []

        def dfs(node, depth):
            if node:
                if len(myList) <= depth:
                    myList.append([0,0])
                myList[depth][0] += node.val
                myList[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return [levSum / levCount for levSum, levCount in myList]
