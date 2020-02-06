"""
1339. Maximum Product of Splitted Binary Tree
https://leetcode.com/contest/weekly-contest-174/problems/maximum-product-of-splitted-binary-tree/
Credits: Alex Wice [https://leetcode.com/awice]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs1(node):
            if not node:
                return 0
            return node.val + dfs1(node.left) + dfs1(node.right)

        self.ans = 0

        def dfs2(node):
            if not node:
                return 0
            t = node.val + dfs2(node.left) + dfs2(node.right)
            self.ans = max(self.ans, t * (dfs_sum - t))
            return t

        dfs_sum = dfs1(root)
        o_ans = dfs2(root)
        return self.ans % (10 ** 9 + 7)