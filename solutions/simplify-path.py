"""
71. Simplify Path

- https://leetcode.com/problems/simplify-path/
- https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/
"""

# Method 1

class Solution:
    def simplifyPath(self, path: str) -> str:
        # split the absolute path with /
        splitPath = path.split("/")
        tempList = []
        # iterate over the split path
        for ch in splitPath:
            # the directory is not empty or not current directory
            if ch is not '' and ch is not '.':
                # for previous directory pop the last directory from tempList if present otherwise continue
                if ch == '..':
                    if tempList: tempList.pop()
                    else: continue
                else:
                    # for all other directory name append them to tempList
                    tempList.append(ch)
        # join the tempList with /
        return  "/" + "/".join(tempList)



# Short version of the above
class Solution:
    def simplifyPath(self, path: str) -> str:
        tempList = []
        for ch in path.split("/"):
            if ch == '..':
                if tempList: tempList.pop()
            elif ch and ch != '.':
                tempList.append(ch)
        return "/" + "/".join(tempList)
