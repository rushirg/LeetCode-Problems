"""
784. Letter Case Permutation

- https://leetcode.com/problems/letter-case-permutation/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/
"""

# Method 1


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        def dfs(i, built):
            if i == len(S):
                self.ans.append(built)
                return
            if S[i].isalpha():
                dfs(i + 1, built + S[i].lower())
            dfs(i + 1, built + S[i].upper())

        self.ans = []
        dfs(0, "")
        return self.ans
