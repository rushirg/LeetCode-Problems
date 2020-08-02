"""
1534. Count Good Triplets
https://leetcode.com/problems/count-good-triplets/
https://leetcode.com/contest/weekly-contest-200/problems/count-good-triplets/
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # here the arr length is not huge
        # so we can use the brute force to get the count as per the condition

        # 0 <= i < j < k < arr.length
        # |arr[i] - arr[j]| <= a
        # |arr[j] - arr[k]| <= b
        # |arr[i] - arr[k]| <= c

        # our count variable to hold the result
        count = 0

        # iterate over i, j, k such that  0 <= i < j < k < arr.length
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    # here we are starting with i/j+1  becasue of the i < j < k < condition
                    # check the other conditions
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1


        # return the count
        return count

