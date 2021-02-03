"""
141. Linked List Cycle
- https://leetcode.com/problems/linked-list-cycle/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627/
"""


# Method 1
# using slow and fast pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # initialize slow and fast pointers to head
        slow = head
        fast = head
        # check if slow, fast and fast next pointers are valid
        while slow and fast and fast.next:
            # update the slow and fast pointers
            slow = slow.next
            fast = fast.next.next
            # check if they are same and return True if they are
            if slow == fast: return True
        return False


# Method 2
# using hashing

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # define a dictionary
        myDict = {}
        # iterate until the head becomes None
        while head:
            # if address already present in dictionary return True
            # hashing
            if head in myDict:
                return True
            # otherwise add the address in dictionary and update head
            myDict[head] = 1
            head = head.next
        return False

