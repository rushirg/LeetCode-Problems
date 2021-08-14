"""
1962. Remove Stones to Minimize the Total

- https://leetcode.com/problems/remove-stones-to-minimize-the-total/submissions 
- https://leetcode.com/contest/weekly-contest-253/problems/remove-stones-to-minimize-the-total/
"""

# Method 1
# using heap (max)
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        from heapq import heappop, heappush, heapify
        heap = []
        heapify(heap)
        for num in piles:
            heappush(heap, -num)
        for i in range(k):
            tmp = -1 * heappop(heap)
            heappush(heap, -(math.ceil(tmp/2)))
        op = 0
        for i in heap:
            op += i
        return -1 * op
        
