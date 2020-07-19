"""
1521. Find a Value of a Mysterious Function Closest to Target
https://leetcode.com/contest/weekly-contest-198/problems/find-a-value-of-a-mysterious-function-closest-to-target/
"""

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:

        # create a set to store our result
        result = set()

        # convert the input array to set to get unique values
        # I will again convert this set to a list
        arr = list(set(arr))

        # base case if we only have one unique element
        if len(arr) is 1:
            return abs(target - arr[0])

        # create a matrix to hold the & operation intermediate result
        # I am just initializing it with -1 as default
        mat = [[-1 for x in range(len(arr))] for x in range(len(arr))]

        # iterate the matrix
        for i in range(len(arr)):
            firstTime = True
            for j in range(i, len(arr)):
                if firstTime:
                    # this conditon is only for index like [0,0], [1,1], [2,2]
                    mat[i][j] = arr[j]
                    result.add(abs(target - arr[j]))
                    firstTime = False
                else:
                    # this case if for all the other combination of index like [0,1],[0,2]...
                    mat[i][j] = mat[i][j - 1] & arr[j]
                    result.add(abs(target - mat[i][j]))
        # we will only need to find the minimum from this result set
        return (min(result))



