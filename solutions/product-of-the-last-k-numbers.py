"""
1352. Product of the Last K Numbers
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


class ProductOfNumbers(object):

    def __init__(self):
        self.myList = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.myList = [1]
        else:
            self.myList.append(self.myList[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if(len(self.myList) > k):
            return self.myList[-1] // self.myList[-k - 1]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)