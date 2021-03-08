"""
344. Reverse String
- https://leetcode.com/problems/reverse-string/
- https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/
"""

# Method 1
# Time: O(N)
# Space: O(N)
# Using stack

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(s, i, j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            return rev(s, i + 1, j - 1)
        return rev(s, 0, len(s)-1)


# Method 2
# Time: O(N)
# Space: O(1)
# Using two pointers - left and right
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


