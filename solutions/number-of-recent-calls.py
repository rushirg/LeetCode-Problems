"""
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/
"""

class RecentCounter:

    def __init__(self):
        # initialize a list to hold all the incoming request time
        self.newRequest = []

    def ping(self, t: int) -> int:
        # calculate the left and right range
        l, r = t - 3000, t

        # add the new request time to the list
        self.newRequest.append(t)

        # iterate over the list and remove any time if lower than l
        # as the incoming order will always be increasing
        for t in self.newRequest:
            if t < l:
                self.newRequest = self.newRequest[1:]
            else:
                break
        return len(self.newRequest)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
