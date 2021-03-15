"""
535. Encode and Decode TinyURL
- https://leetcode.com/problems/encode-and-decode-tinyurl/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/
"""

# Method 1
# storing random unique alphanumeric string of length N in dictionary

import string
import random
import time
class Codec:

    def __init__(self):
        self.myDict = {}
        self.rawData = string.ascii_letters + string.digits
        self.length = 7
        self.urlTemplate = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            shortUrl = ""
            for i in range(self.length):
                shortUrl += random.choice(self.rawData)
            if shortUrl not in self.myDict:
                self.myDict[shortUrl] = longUrl
                break

        return self.urlTemplate + shortUrl


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.myDict[shortUrl.split("/")[-1]]
