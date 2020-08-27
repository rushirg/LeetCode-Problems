"""
412. Fizz Buzz
- https://leetcode.com/problems/fizz-buzz/
- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3437/
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # create a result list
        result = []

        # iterate till n
        for i in range(1, n + 1):

            # check for multiple of 5 and 3
            if i % 3 == 0and i % 5 == 0:
                result.append("FizzBuzz")
            # if multiple of 3
            elif i % 3 == 0:
                result.append("Fizz")
            # if multiple of 5
            elif i % 5 == 0:
                result.append("Buzz")
            # include rest of integers as their string representation
            else:
                result.append(str(i))

        # return our result
        return result

