"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = None
        carry = 0
        digitSum = 0
        root = True
        while(l1 != None and l2 != None):
            tmp = l1.val + l2.val
            if (carry):
                tmp += 1
                carry = 0
            if(tmp > 9):
                carry = 1
                tmp %= 10

            if(ans == None):
                ans = ListNode(tmp)
                root = ans
            else:
                ans.next = ListNode(tmp)
                ans = ans.next
            l1 = l1.next
            l2 = l2.next

        while(l1 != None):
            if(carry != 0):
                updateval = l1.val + carry
                carry = 0
                if(updateval > 9):
                    ans.next = ListNode(updateval % 10)
                    carry = 1
                else:
                    ans.next = ListNode(updateval)
            else:
                ans.next = ListNode(l1.val)
            ans = ans.next
            l1 = l1.next
        while(l2 != None):
            if(carry != 0):
                updateval = l2.val + carry
                carry = 0
                if(updateval > 9):
                    ans.next = ListNode(updateval % 10)
                    carry = 1
                else:
                    ans.next = ListNode(l2.val + 1)
            else:
                ans.next = ListNode(l2.val)
            ans = ans.next
            l2 = l2.next

        if (carry !=0 ):
            ans.next = ListNode(carry)
            carry = 0
        return root


