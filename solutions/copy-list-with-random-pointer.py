"""
138. Copy List with Random Pointer

- https://leetcode.com/problems/copy-list-with-random-pointer/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/
"""

# Method 1
# Time complexity: O(n) with Space Complexity: O(1) excluding the copy node space

"""
#Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        node = head
        while node:
            nodeNext = node.next
            node.next = Node(node.val, nodeNext, None)
            node = nodeNext

        node = head
        while node:
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next

        node = head
        copyHead = head.next
        copyNode = copyHead

        while copyNode.next:
            node.next = node.next.next
            node = node.next

            copyNode.next = copyNode.next.next
            copyNode = copyNode.next
        node.next = node.next.next
        return copyHead



# Method 2
# Time complexity: O(N) with Space complexity: O(N)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        dic, node = {}, head
        while node:
            dic[node] = Node(node.val, None, None)
            node = node.next

        node = head
        while node:
            if node.next:
                dic[node].next = dic[node.next]
            if node.random:
                dic[node].random = dic[node.random]
            node = node.next

        return dic[head]


# Method 3
# Time complexity: O(N) with Space complexity: O(N)
# Dictionary/Map method

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic, prev, node = {}, None, head
        while node:
            if node not in dic:
                dic[node] = Node(node.val, node.next, node.random)
            if prev is None:
                head = dic[node]
            else:
                prev.next = dic[node]
            if node.random:
                if node.random not in dic:
                    dic[node.random] = Node(node.random.val, node.random.next, node.random.random)
                dic[node].random = dic[node.random]
            prev, node = dic[node], node.next
        return head
