"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

# Solution 1:
# Time Complexity: O(N log N)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted[x * x for x in A]





# Solution 2:
# Time ComplexityL O(N)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        LenA = len(A)
        j = 0

        # j will hold the first positive number's index
        while j < LenA and A[j] < 0:
            j += 1

        # i will hold the highest negative number
        i = j - 1

        # output list to hold resultant array
        output = []

        while i >= 0 and j < LenA:
            if A[i]**2 < A[j]**2:
                output.append(A[i]**2)
                i -= 1
            else:
                output.append(A[j]**2)
                j += 1

        # if there are still some element left unvisited
        while i >= 0:
            output.append(A[i]**2)
            i -= 1
        while j < LenA:
            output.append(A[j]**2)
            j += 1

        # return output list
        return output

