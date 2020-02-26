"""
1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        mydict = defaultdict(list)

        for i in range(len(groupSizes)):
            mydict[groupSizes[i]].append(i)

        ans = list()
        for i in mydict.keys():
            a_ans = mydict[i]
            for j in range(len(a_ans) // i):
                b_ans = a_ans[i * j: i * (j + 1)]
                ans.append(b_ans)
        return(ans)
