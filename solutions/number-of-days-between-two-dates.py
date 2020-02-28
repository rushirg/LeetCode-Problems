"""
1360. Number of Days Between Two Dates
https://leetcode.com/problems/number-of-days-between-two-dates/
"""
from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1, date2 = date1.split("-"), date2.split("-")
        d1, d2 = date(int(date1[0]), int(date1[1]), int(date1[2])), date(int(date2[0]), int(date2[1]), int(date2[2]))
        return(abs((d1-d2).days))
