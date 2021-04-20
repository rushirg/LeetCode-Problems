"""
589. N-ary Tree Preorder Traversal
- https://leetcode.com/problems/n-ary-tree-preorder-traversal/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/
"""

# Method 1
# iterative

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        self.mylist = []
        self.result = []
        def dfs(node):
            while node:
                if node.children:
                    self.mylist = list(node.children) + self.mylist
                self.result.append(node.val)
                if self.mylist:
                    node = self.mylist.pop(0)
                else:
                    return

        dfs(root)
        return self.result



# Method 2
# recursive

class Solution:
    def dfs(self, root, result):
        if root is None:
            return
        result.append(root.val)
        for child in root.children:
            self.dfs(child, result)

    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.dfs(root, result)
        return result
