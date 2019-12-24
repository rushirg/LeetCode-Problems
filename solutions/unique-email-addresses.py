"""
Solution for problem 929
https://leetcode.com/problems/unique-email-addresses/
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailsSet = set()
        for ids in emails:
            name, domain = ids.split('@')
            name = (name.split("+")[0]).replace(".", "")
            emailsSet.add(name+"@"+domain)
        return len(emailsSet)

