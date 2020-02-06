"""
1337. The K Weakest Rows in a Matrix
https://leetcode.com/contest/weekly-contest-174/problems/the-k-weakest-rows-in-a-matrix/
"""

# Method 1
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        tmp = dict()
        for i in range(len(mat)):
            tmp[i] = mat[i].count(0)
        ans = list()
        for i in range(k):
            keymax = max(tmp, key=tmp.get)
            ans.append(keymax)
            tmp.pop(keymax, None)
        return(ans)


# Method 2
# Credit: Alex Wice [https://leetcode.com/awice]
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        arr = [(sum(row), i) for i, row in enumerate(mat)]
        arr.sort()
        return[i for _, i in arr[:k]]
