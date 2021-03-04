"""
941. Valid Mountain Array
- https://leetcode.com/problems/valid-mountain-array
- https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
"""

# Method 1
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

    # A.length >= 3
    # There exists some i with 0 < i < A.length - 1 such that:
    #     A[0] < A[1] < ... A[i-1] < A[i]
    #     A[i] > A[i+1] > ... > A[A.length - 1]
        if len(A) < 3:
            return False
        flag = True
        index = None
        for i in range(1, len(A) - 1):
            if A[i - 1] <  A[i] and A[i] > A[i + 1]:
                index = i
                break
        if index == None:
            return False

        for i in range(index, 0, -1):
            if A[i] <= A[i - 1]:
                return False

        for i in range(index, len(A) - 1):
            if A[i] <= A[i + 1]:
                return False

        return True



# Method 2

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walking up
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peek can't be first or last
        if i == 0 or i == N-1:
            return False

        # walking down
        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N-1



