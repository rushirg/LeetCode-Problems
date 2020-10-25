"""
1261. Find Elements in a Contaminated Binary Tree
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
"""


# Solution 1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        def createTree(root, value):
            if root == None:
                return
            if root.left != None:
                root.left.val = 2 * value + 1
                self.valueDict[root.left.val] = 1
                createTree(root.left, root.left.val)
            if root.right != None:
                root.right.val = 2 * value + 2
                self.valueDict[root.right.val] = 1
                createTree(root.right, root.right.val)

        self.root = root
        self.root.val = 0
        self.valueDict = {}
        self.valueDict[self.root.val] = 1
        if self.root.left or self.root.right:
            createTree(self.root, self.root.val)

    def find(self, target: int) -> bool:
        return target in self.valueDict

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
