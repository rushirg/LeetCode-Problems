"""
1418. Display Table of Food Orders in a Restaurant
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""

# Solution 1

from collections import Counter
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tableDict = {}
        foodItems = set()
        for order in orders:
            if int(order[1]) in tableDict:
                tableDict[int(order[1])].append(order[2])
            else:
                tableDict[int(order[1])] = [order[2]]
            foodItems.add(order[2])
        result = []
        foodItems = list(foodItems)
        foodItems.sort()
        result.append(["Table"] + foodItems)


        for t in sorted(tableDict):
            tmpResult = [str(t)]
            itemCounter = Counter(tableDict[t])
            for item in foodItems:
                if item in itemCounter:
                    tmpResult.append(str(itemCounter[item]))
                else:
                    tmpResult.append("0")
            result.append(tmpResult)
        return result
