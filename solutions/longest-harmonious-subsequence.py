"""
594. Longest Harmonious Subsequence
- https://leetcode.com/problems/longest-harmonious-subsequence/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/
"""


# Method 1
"""
We need not care about key − 1, because if key is present in the harmonic subsequence, at one time either key + 1 or key - 1 only could be included in the harmonic subsequence.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # create a counter object for all the numbers in the list
        cnt = collections.Counter(nums)
        ans = 0
        # iterate over the counter keys
        for x in cnt:
            # check if the current number + 1 exits
            if x + 1 in cnt:
                # take max of sum of counter or the current answer
                ans = max(ans, cnt[x] + cnt[x + 1])
        return ans



# Method 2
"""
one loop with out Counter object
We consider both the key - 1 and key + 1 in this case because it could be possible that key has already been added to the map and later on key - 1 is encountered, this would result in wrong output
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # define empty dictionary and result variable
        cnt = {}
        res = 0
        # iterate list element by element
        for n in nums:
            # if new number, create key with count value to 1
            if n not in cnt:
                cnt[n] = 1
            else:
                # alredy exists increment the counter for that number
                cnt[n] += 1
            # if key + 1 exits update result with max of current number count + next number count
            if (n + 1 in cnt):
                res = max(res, cnt[n + 1] + cnt[n])
            # if key - 1 exits update result with max of current number count + previous number count
            if (n - 1 in cnt):
                res = max(res, cnt[n - 1] + cnt[n])
        return res
