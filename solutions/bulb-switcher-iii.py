"""
1375. Bulb Switcher III
https://leetcode.com/problems/bulb-switcher-iii/
"""
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        mx = -1
        for i, x in enumerate(light, 1):
            mx = max(x, mx)
            if mx == i:
                count += 1
        return count
