"""
714. Best Time to Buy and Sell Stock with Transaction Fee
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3674/
"""

# Method 1
# Using DP

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
