"""
1209. Remove All Adjacent Duplicates in String II
- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
- https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3710/
"""

# Method 1
# Using stack to store the character and count
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        myStack = [(s[0], 1)]
        count = 1
        for i in range(1, len(s)):
            if myStack and myStack[-1][0] == s[i]:
                myStack.append((s[i], myStack[-1][1] + 1))
            else:
                count = 1
                myStack.append((s[i], count))
            if myStack[-1][1] == k:
                myStack = myStack[:len(myStack) - k]
        result = ""
        for ch in myStack:
            result += ch[0]
        return result


# Slight variation in above method
# do not push the same character in the stack instead increment its value
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        myStack = [['#', 0]]
        for ch in s:
            if myStack[-1][0] == ch:
                myStack[-1][1] += 1
                if myStack[-1][1] == k:
                    myStack.pop()
            else:
                myStack.append([ch, 1])

        return "".join(c * k for c, k in myStack)
