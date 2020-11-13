"""
https://leetcode.com/problems/design-parking-system/
1603. Design Parking System
"""

# Method 1:
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.capacity[carType - 1] == 0:
            return False
        self.capacity[carType - 1] -= 1;
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
