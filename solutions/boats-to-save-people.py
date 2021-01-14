"""
881. Boats to Save People
https://leetcode.com/problems/boats-to-save-people/
https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3602/
Medium
"""

# Method 1
# O(nlogn)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the people list
        peopleSort = sorted(people)
        start = 0
        boats = 0
        end = len(peopleSort) - 1
        while start < end:
            # person's weight is equal to limit of the boat
            if peopleSort[end] == limit:
                boats += 1
                end -= 1
            # if heavy and light weight person can fit in a boat
            elif peopleSort[end] + peopleSort[start] <= limit:
                boats += 1
                start += 1
                end -= 1
            # if only heavy person can fit in a boat
            else:
                boats += 1
                end -= 1
        # if any remaining person, he will go alone in a boat
        if start == end:
            boats += 1
        return boats



# Method 2
# Removing redundant checks from Method 1
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sortedPeople = sorted(people)
        start, end = 0, len(sortedPeople) - 1
        boats = 0
        while start <= end:
            if (sortedPeople[start] + sortedPeople[end]) <= limit:
                start += 1
            boats += 1
            end -= 1
        return boats
                


# Method 3
# Using buckets method instead of sorting
# logic is same only same only storing the count of the same weight person 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        buckets = [0] * (limit + 1)
        for n in people:
            buckets[n] += 1
        start, end = 0, len(buckets) - 1
        boats = 0
        while start <= end:
            while (start <= end) and buckets[start] <= 0:
                start += 1
            while (start <= end) and buckets[end] <= 0:
                end -= 1
            if buckets[start] <= 0 and buckets[end] <= 0:
                break
            boats += 1
            if (start + end) <= limit:
                buckets[start] -= 1
            buckets[end] -= 1

        return boats
