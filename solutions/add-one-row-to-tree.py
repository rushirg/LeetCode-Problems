"""
623. Add One Row to Tree
- https://leetcode.com/problems/add-one-row-to-tree/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/
"""

# Method 1
# using DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        def dfs(node, v, d, height):
            if node:
                if height == d - 1:
                    newNode = TreeNode(v)
                    newNode.left = node.left
                    node.left = newNode

                    newNode2 = TreeNode(v)
                    newNode2.right = node.right
                    node.right = newNode2

                else:
                    dfs(node.left, v, d, height+1)
                    dfs(node.right, v,d,  height+1)


        if d == 1:
            newNode = TreeNode(v, root)
            return newNode

        dfs(root, v, d, 1)
        return root


# Similar to above but storing the original node if dfs method
def dfs(node, v, d, height):
            if node:
                if height == d - 1:
                    tmp = node.left
                    node.left = TreeNode(v)
                    node.left.left = tmp

                    tmp = node.right
                    node.right = TreeNode(v)
                    node.right.right = tmp
                else:
                    dfs(node.left, v, d, height+1)
                    dfs(node.right, v,d,  height+1)


