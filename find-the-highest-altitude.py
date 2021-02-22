"""
1732. Find the Highest Altitude
- https://leetcode.com/problems/find-the-highest-altitude/
"""

# Method 1

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        altitudeSum = 0
        for height in gain:
            altitudeSum += height
            # instead of if block we can directly use max
            # altitude = max(altitudeSum, altitude)
            if altitudeSum > altitude: altitude = altitudeSum
        return altitude



