"""
102. Binary Tree Level Order Traversal
- https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Method 1
# Using List
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        temp = [root]
        while temp:
            ans = []
            temp2 = []
            for i in range(len(temp)):
                ans.append(temp[i].val)
                if temp[i].left: temp2.append(temp[i].left)
                if temp[i].right: temp2.append(temp[i].right)
            result.append(ans)
            temp = temp2
        return result
