"""
538. Convert BST to Greater Tree

- https://leetcode.com/problems/convert-bst-to-greater-tree/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/
"""

# Method 1
# Reverse Inorder traversal with a global total variable

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def revInorder(root):
            if root:
                revInorder(root.right)
                self.total = root.val + self.total
                root.val = self.total
                revInorder(root.left)

        revInorder(root)
        return root
