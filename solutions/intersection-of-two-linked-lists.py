"""
160. Intersection of Two Linked Lists
- https://leetcode.com/problems/intersection-of-two-linked-lists
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/
"""

# Method 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next

            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next

        return nodeA


# Method 2
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        def getLen(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        lenA = getLen(headA)
        lenB = getLen(headB)

        while lenA > lenB:
            headA = headA.next;
            lenA -= 1

        while lenA < lenB:
            headB = headB.next
            lenB -= 1


        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


