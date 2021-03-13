"""
1329. Sort the Matrix Diagonally
- https://leetcode.com/problems/sort-the-matrix-diagonally/
"""

# Method 1
# storing and processing the diagonal values

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def diagonalSort(mat, count, row, col, i, j):
            while count:
                tmp, tmpi, tmpj = [], i, j
                while tmpi < row and tmpj < col:
                    tmp.append(mat[tmpi][tmpj])
                    tmpi += 1; tmpj += 1
                tmp.sort()
                tmpi, tmpj = i, j
                while tmpi < row and tmpj < col:
                    if i:
                        mat[tmpi][tmpj] = tmp[tmpj]
                    else:
                        mat[tmpi][tmpj] = tmp[tmpi]
                    tmpi += 1; tmpj += 1
                count -= 1
                if i: i += 1
                else: j += 1
        r, c = len(mat), len(mat[0])
        # for diagonals starting from row 0 and onwards
        diagonalSort(mat, c, r, c, i=0, j=0)
        # for diagonals starting from row 1, coloum 0 and onwards
        diagonalSort(mat, r-1, r, c, i=1, j=0)
        return mat

