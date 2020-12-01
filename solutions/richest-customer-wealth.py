"""
1672. Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/
https://leetcode.com/contest/weekly-contest-217/problems/richest-customer-wealth/
"""


### Method 1
"""
Iterating over the list
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # consider the wealth is negative as given condition is 1<= accounts[i][j] <=100
		wealth = -1
		# iterate over all the accounts
        for acc in accounts:
			# update the max wealth
            wealth = max(wealth, sum(acc))
		return wealth
"""
or other way
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # create a list of sum of wealth from all accounts and then return max
		max([sum(acc) for acc in accounts])


### Method 2
"""
using map
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # use sum function on accounts iterables and then calculating max 
		return max(map(sum, accounts))

