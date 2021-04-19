"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""


# Method 1
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # newValue = v1 + v2 + carry
            # carry = newValue // 10
            # newValue = newValue % 10
            carry, newValue = divmod(v1 + v2 + carry, 10)
            n.next  = ListNode(newValue)
            n = n.next
        return result.next
                

# Method 2
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # newValue = v1 + v2 + carry
            # carry = newValue // 10
            # newValue = newValue % 10
            carry, newValue = divmod(v1 + v2 + carry, 10)
            n.next  = ListNode(newValue)
            n = n.next
        return result.next



# Method 2

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


