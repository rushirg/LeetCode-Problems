"""
966. Vowel Spellchecker
- https://leetcode.com/problems/vowel-spellchecker/
- https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/
"""

# Method 1
# Using Hashing/Dictionary and mask for vowel errors

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def maskVowels(word):
            return "".join('*' if c in 'aeiou' else c for c in word)

        wordlistDict = set(wordlist)
        lowerWordlistDict = {}
        wordMask = {}

        for word in wordlist:
            lowerWord = word.lower()
            lowerWordlistDict.setdefault(lowerWord, word)
            wordMask.setdefault(maskVowels(lowerWord), word)

        answer = []
        for query in queries:
            # 1st
            if query in wordlistDict:
                answer.append(query)
                continue

            # 2nd
            lowerQuery = query.lower()
            if lowerQuery in lowerWordlistDict:
                answer.append(lowerWordlistDict[lowerQuery])
                continue

            # 3rd
            queryMask = maskVowels(lowerQuery)
            if queryMask in wordMask:
                answer.append(wordMask[queryMask])
            else:
                # 4th
                answer.append("")
        return answer


