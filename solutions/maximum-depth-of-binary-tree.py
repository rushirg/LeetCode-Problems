"""
104. Maximum Depth of Binary Tree
- https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Method 1
# Using DFS

class Solution(object):
    def dfs(self, node, depth):
        if not node:
            return depth - 1
        return max(self.dfs(node.left, depth + 1), self.dfs(node.right, depth + 1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.dfs(root, 1)
