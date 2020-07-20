"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # lets store our head in a temporary variable and a previous variable
        tmp = head
        prev = head

        # loop until tmp node is not None:
        while tmp != None:

            # check if node value is equal to given value
            if tmp.val == val:

                # check if starting node has same value as value
                if tmp == head:
                    # update the head as the starting value has same value as given val
                    head = tmp.next
                    prev = tmp.next
                else:
                    # for all the other cases
                    prev.next = tmp.next

                # move ahead the node
                tmp = tmp.next
            else:
                # if node has not same value
                # update the previous node and next node
                prev = tmp
                tmp = tmp.next

        # return the head node
        return head
