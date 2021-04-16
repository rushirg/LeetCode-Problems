"""
86. Partition List
- https://leetcode.com/problems/partition-list/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3707/
"""


# Method 1
# Using two pointers
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessX = lessThanX = ListNode(0)
        greatX = greaterThanX = ListNode(0)

        while head:
            if head.val < x:
                lessX.next = head
                lessX = lessX.next
            else:
                greatX.next = head
                greatX = greatX.next
            head = head.next

        # last node of greaterThanX would be None
        greatX.next = None

        # append lesssThanX list to the next
        lessX.next = greaterThanX.next

        return lessThanX.next




# Method 2
# Using two list to store greater than and less than X
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return head
        greaterThanX = []
        lessThanX = []
        node = head
        while node:
            if node.val < x:
                lessThanX.append(node.val)
            elif node.val >= x:
                greaterThanX.append(node.val)
            node = node.next
        node = head
        while node:
            if lessThanX:
                newNodeValue = lessThanX.pop(0)
                node.val = newNodeValue
            elif greaterThanX:
                newNodeValue = greaterThanX.pop(0)
                node.val = newNodeValue
            node = node.next
        return head
