"""
1461. Check If a String Contains All Binary Codes of Size K
- https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/
"""

# Method 1
# Using set

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        mySet = set()
        for i in range(len(s) - k + 1):
            mySet.add(s[i:i+k])
        return len(mySet) == (2 ** k)
        # otherwise
        # return len(mySet) == 1 << k
    
