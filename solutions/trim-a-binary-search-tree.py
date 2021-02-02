"""
669. Trim a Binary Search Tree

- https://leetcode.com/problems/trim-a-binary-search-tree/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/

"""

# Method 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def inorder(root):
            # for no None values
            if root:
                # if node value is less than low, trim the left side
                if root.val < low:
                    return inorder(root.right)  
                # if node value is greater than high, trim the right side
                if root.val > high:
                    return inorder(root.left)
                else:
                    # otherwise trim both left and right side
                    root.left = inorder(root.left)
                    root.right = inorder(root.right)
                    return root
        return inorder(root)
         
