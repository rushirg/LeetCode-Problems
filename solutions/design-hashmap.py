"""
706. Design HashMap
https://leetcode.com/problems/design-hashmap/
"""


### Solution 1

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myHashMap = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.myHashMap[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.myHashMap[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.myHashMap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)





### Solution 2

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myHashMap = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.myHashMap[key] = value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.myHashMap:
            return self.myHashMap[key]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # Another way to delete but this is slower than pop method
        """
        if key in self.myHashMap: 
            del self.myHashMap[key]
        """
            self.myHashMap.pop(key, None)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
