"""
1302. Deepest Leaves Sum

- https://leetcode.com/problems/deepest-leaves-sum/
"""

# Method 1
# Level order traversal

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        prevSum = root.val
        while len(queue) != 0:
            tempQ = []
            levelSum = 0
            for node in queue:
                if node.left:
                    tempQ.append(node.left)
                    levelSum += node.left.val
                if node.right:
                    tempQ.append(node.right)
                    levelSum += node.right.val
            if levelSum:
                prevSum = levelSum
            queue = tempQ
        return prevSum



# Method 2
# DFS traversal 

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return 0
            return max(1 + height(node.left), 1 + height(node.right))

        self.mySum = 0
        def dfs(node, height=0):
            if node:
                if (treeHeight-1) == height:
                    self.mySum += node.val
                dfs(node.left, height + 1)
                dfs(node.right, height + 1)

        treeHeight = height(root)
        dfs(root)
        return self.mySum
