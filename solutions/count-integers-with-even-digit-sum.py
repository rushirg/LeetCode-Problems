"""
2180. Count Integers With Even Digit Sum

https://leetcode.com/contest/weekly-contest-281/problems/count-integers-with-even-digit-sum/
https://leetcode.com/problems/count-integers-with-even-digit-sum/
"""

# Method 1
# Iterative approach

class Solution:
    def countEven(self, num: int) -> int:
        
        def getDidgitSum(num):
            digitSum = 0
            while(num > 0):
                digitSum += num % 10
                num //= 10
            return digitSum
        
        total = 0
        for i in range(1, num+1):
            digitSum = getDidgitSum(i)
            if digitSum % 2 == 0:
                total += 1
        return total


# Method 2
# convert number to string and iterating over

class Solution:
    def countEven(self, num: int) -> int:
        
        def getDidgitSum(num):
            digitSum = 0
            for digit in str(num):
                digitSum += int(digit)
            return digitSum
            
        total = 0
        for i in range(1, num+1):
            digitSum = getDidgitSum(i)
            if digitSum % 2 == 0:
                total += 1
        return total
