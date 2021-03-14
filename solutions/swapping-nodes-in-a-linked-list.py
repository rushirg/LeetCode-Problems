"""
1721. Swapping Nodes in a Linked List
- https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/
"""

# Method 1
# using list to store the linked list values
# 2 pass

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        node = head
        valList = []
        while node:
            valList.append(node.val)
            node = node.next

        valList[k-1], valList[len(valList) - k] = valList[len(valList) - k], valList[k-1]

        node = head
        i = 0
        while node:
            node.val = valList[i]
            i += 1
            node = node.next
        return head



# Method 2
# one pass
# if reached at Kth node, keep traversing from head till reach last node

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1, n2, p = None, None, head
        while p is not None:
            k -= 1
            n2 = None if n2 == None else n2.next
            if k == 0:
                n1 = p
                n2 = head
            p = p.next

        n1.val, n2.val = n2.val, n1.val
        return head


# Method 3
# Using slow and fast pointers
# first set first value to k-1 node, then start slow and fast till fast reaches last node, second node would be at slow pointer 

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow = fast = first = second = head

        for i in range(k - 1):
            fast = fast.next

        first = fast

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        second = slow

        first.val, second.val = second.val, first.val
        return head
