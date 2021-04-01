"""
234. Palindrome Linked List
- https://leetcode.com/problems/palindrome-linked-list/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/
"""

# Method 1
# Time: O(N), Space: O(N)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        myList = []
        node = head
        while node:
            myList.append(node.val)
            node = node.next
        return myList == myList[::-1]


# Method 2
# Time: O(N), Space: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        # find middle node with slow and fast pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half list/right side list
        node = None
        while slow:
            nextNode =  slow.next
            slow.next = node
            node = slow
            slow = nextNode

        # check from new revered list with head, if values didn't match return
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
