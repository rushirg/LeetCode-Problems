"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Let's use a queue here to traverse the tree in level order
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        # declare the output list, it willhold the final result
        output = []

        # another list to hold temorary node values, initialize with the root node
        temp = [root]

        # I FORGOT THAT WE HAVE TO TRAVERSE ZIG ZAG
        # define a flag, intialize it with zig and alternatively change the flag
        flag = "zig"

        # loop until this temp/temporay list lenght is 0
        while len(temp) != 0:

            # declare another list to hold the level order tree values
            op = []

            # loop to the length of your temporay list length
            # this ensures the queue like operation as we will deque/remove only those values who are on same level
            for i in range(len(temp)):

                # pop out the first value
                node = temp.pop(0)

                # if valid node, add its left and right childern and append the value in intermediate list
                if node:
                    op.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)


            # this ensures that we have some values in the intermediate list
            if len(op) != 0:
                if flag == "zig":
                    output.append(op)
                    flag = "zag"
                else:
                    output.append(op[::-1])
                    flag = "zig"
        # THIS WAS MY MISTAKE i WAS RETURNING IN THE WHILE LOOP THATS WHY IT WAS ONLY RETURNING ME FIRST ELEMENT ONLY
        return output
