"""
841. Keys and Rooms
- https://leetcode.com/problems/keys-and-rooms/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3677/
"""

# Method 1

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        totalRooms = len(rooms)
        visitRoom = {0:1}
        checkRoom = []
        for room in rooms[0]:
            checkRoom.append(room)

        while checkRoom:
            room = checkRoom.pop(0)
            if room in visitRoom:
                continue
            visitRoom[room] = 1
            for r in rooms[room]:
                checkRoom.append(r)
        return len(visitRoom.keys()) == totalRooms



