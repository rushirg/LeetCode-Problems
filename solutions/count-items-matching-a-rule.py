"""
1773. Count Items Matching a Rule
- https://leetcode.com/problems/count-items-matching-a-rule/
"""

# Method 1
# Sequential

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keyDict = {
            "type" :    0,
            "color" :   1,
            "name" :    2
        }
        ruleKeyValue = keyDict[ruleKey]
        count = 0
        for item in items:
            if item[ruleKeyValue] == ruleValue:
                count += 1
        return count
