"""
1337. The K Weakest Rows in a Matrix
- https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/
"""

# Method 1

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        for s in range(len(mat)):
            dic[s] = mat[s].count(1)
        weakRow = sorted(dic, key=dic.get)
        return weakRow[:k]


# Method 2

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


# Method 3

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
