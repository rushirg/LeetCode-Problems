"""
2696. Minimum String Length After Removing Substrings

Problem: https://leetcode.com/contest/weekly-contest-346/problems/minimum-string-length-after-removing-substrings/
"""

# Python3

# Approach 1 - Using string as stack
def minLength(self, s: str) -> int:
  tempStr = ''
  for ch in s:
      tempStr += ch
      if(len(tempStr) >= 2):
          index = len(tempStr) - 2
          if(tempStr[index:] == "AB" or tempStr[index:] == "CD"):
              tempStr = tempStr[:index]
  return len(tempStr)


# Approach 2 - Using stack
def minLength(self, s: str) -> int:
  stack = []
  for ch in s:
      if(len(stack) > 0 and ((ch == 'B' and stack[-1] == 'A') or (ch == 'D' and stack[-1] == 'C'))):
         stack.pop()
      else:
         stack.append(ch)
  return len(stack)

