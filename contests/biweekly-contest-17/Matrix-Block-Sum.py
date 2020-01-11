"""
1314. Matrix Block Sum

Problem: https://leetcode.com/contest/biweekly-contest-17/problems/matrix-block-sum/
"""
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
K = 1
m, n = len(mat), len(mat[0])
ans = list()
aux = [[0 for i in range(n)] for j in range(m)]


def preProcess(mat, aux):
    for i in range(0, n, 1):
        aux[0][i] = mat[0][i]
    for i in range(1, m, 1):
        for j in range(0, n, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]
    for i in range(0, m, 1):
        for j in range(1, n, 1):
            aux[i][j] += aux[i][j - 1]


def sumQ(aux, tli, tlj, rbi, rbj):
    res = aux[rbi][rbj]
    if (tli > 0):
        res = res - aux[tli - 1][rbj]
    if (tlj > 0):
        res = res - aux[rbi][tlj - 1]
    if (tli > 0 and tlj > 0):
        res = res + aux[tli - 1][tlj - 1]
    return res


preProcess(mat, aux)

for i in range(m):
    r = list()
    for j in range(n):
        r_lower = i - K
        if r_lower < 0:
            r_lower = 0
        r_upper = i + K
        if r_upper >= m:
            r_upper = m - 1
        j_lower = j - K
        if j_lower < 0:
            j_lower = 0
        j_upper = j + K
        if j_upper >= n:
            j_upper = n - 1
        tmp = 0
        r.append(sumQ(aux, r_lower, j_lower, r_upper, j_upper))
    ans.append(r)
print(ans)
