"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Solution 1
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



# Method 2
# Using Stack - Iterative
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        node = root
        while node != None or stack:
            while node != None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
