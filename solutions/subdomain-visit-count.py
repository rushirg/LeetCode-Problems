"""
811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/
"""

### Solution 1
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        myDict = {}
        for w in cpdomains:
            count, domain = w.split()
            if domain in myDict:
                myDict[domain] += int(count)
            else:
                myDict[domain] = int(count)

            topDomain = domain.split(".")[1:]
            for i in range(len(topDomain)):
                tdomain = ".".join(topDomain)
                if tdomain in myDict:
                    myDict[tdomain] += int(count)
                else:
                    myDict[tdomain] = int(count)
                topDomain.pop(0)

        result = []
        for k, v in myDict.items():
            result.append(str(v) +" " + k)

        return result
