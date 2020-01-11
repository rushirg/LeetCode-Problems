"""
1313. Decompress Run-Length Encoded List

Problem: https://leetcode.com/contest/biweekly-contest-17/problems/decompress-run-length-encoded-list/
"""

nums = [1, 2, 3, 4]
ans = list()
i = 0
while (2 * i + 1) < len(nums):
    ans += [nums[2 * i + 1] for x in range(nums[2 * i])]
    i += 1
print(ans)
