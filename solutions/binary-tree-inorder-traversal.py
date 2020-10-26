"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Solution 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def inorder(root, result):
            if root:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)

        inorder(root, result)
        return result
