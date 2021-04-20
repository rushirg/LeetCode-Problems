"""
42. Trapping Rain Water
- https://leetcode.com/problems/trapping-rain-water/
"""

# Method 1
# DP

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        ans = 0
        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])

        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])

        for i in range(1, len(height)):
            ans += min(left[i], right[i]) - height[i]

        return ans
