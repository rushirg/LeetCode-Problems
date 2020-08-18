"""
1103. Distribute Candies to People
- https://leetcode.com/problems/distribute-candies-to-people/
- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3427/
"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # create an array of size num_people and initialize it with 0
        list_people = [0] * num_people

        # starting/initial value of n
        index = 1

        # iterate until the number of candies are more than 0
        while candies > 0:

            # if candies are more than index value, add the index value to the location
            if candies > index:
                # we are using mod operation to index by the num_people to locate the index of the array
                # we are subtracting by 1 because the array index starts at 0
                list_people[(index - 1) % num_people] += index
            else:
                # if candies are less than index value, add all remaining candies to location
                list_people[(index - 1) % num_people] += candies

            # subtract the candies with index values
            candies -= index

            # increment the index values
            index += 1

        # return the resultant array
        return(list_people)
