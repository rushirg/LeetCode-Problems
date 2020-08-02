"""
705. Design HashSet
https://leetcode.com/problems/design-hashset/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myDict = {}


    def add(self, key: int) -> None:
        self.myDict[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.myDict[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.myDict:
            return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
