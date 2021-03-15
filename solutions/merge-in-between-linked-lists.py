"""
1669. Merge In Between Linked Lists
- https://leetcode.com/problems/merge-in-between-linked-lists/
"""

# Method 1

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = nextNode =  None

        node = list1
        count = 1
        while node.next:
            if count == a:
                prev = node
            if count  == b + 1:
                nextNode = node.next
            node = node.next
            count += 1

        prev.next = list2
        node2 = list2
        end = None
        while node2:
            end = node2
            node2 = node2.next
        end.next = nextNode
        return list1


# Method 2
# slight updated/shorter version than method 1

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # define temporary variables to store prev node of a
        # and next node of b
        prevNode1 = nextNode1 = None

        # define counter
        count = 1
        node = list1

        # traverse list1
        while node:
            # if ath node, store the address
            if count == a:
                prevNode1 = node
            # if bth node, store the bth next node address
            if count == b + 1:
                nextNode1 = node.next
            node = node.next
            count += 1

        # update the ath next to list2 head
        prevNode1.next = list2

        # traverse list2 to get last node
        while list2.next:
            list2 = list2.next

        # update list2 last node next with bth next (nextNode1)
        list2.next = nextNode1
        return list1
