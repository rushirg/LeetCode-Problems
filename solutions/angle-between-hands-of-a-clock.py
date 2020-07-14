"""
1344. Angle Between Hands of a Clock
https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # let's find the angle made by hour hand with
        # hour hand will cover 360 degree in 12 hours i.e. 360 degrees in 12 * 60 minutes
        # let's find how much it will make in a minute
        # convert the hour into minutes and add minutes to total minutes as the hour hand
        # hand will move too in that case
        hourAngle = (360 / (12 * 60)) * (hour * 60 + minutes)


        # now, let's find the angle minute hand will make
        # minute hand will cover 360 degrees in 1 hour i.e 60 minutes
        # i.e. it will make 360/60 = 6 degree in a minute
        minuteAngle = (360/60) * minutes

        # subtract both the angle and take their modulus
        angle = abs(hourAngle - minuteAngle)

        # return the minumium angle
        return min(360 - angle, angle)
