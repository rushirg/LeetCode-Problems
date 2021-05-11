"""
204. Count Primes
- https://leetcode.com/problems/count-primes/
- https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3738/
"""

# Method 1
# Using Sieve of Eratosthenes algorithm

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)

