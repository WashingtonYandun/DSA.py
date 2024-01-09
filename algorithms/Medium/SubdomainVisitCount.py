# 811. Subdomain Visit Count
'''
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
'''

class Solution:
    # 50ms, Beats 93.14%
    # 17.41MB, Beats 6.93%
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}
        for cpd in cpdomains:
            l = cpd.split(" ")
            n = int(l[0])

            parts = l[1].split('.')
            parts_sets = []

            for i in range(len(parts)):
                s = '.'.join(parts[i:])
                parts_sets.append(s)

            for i in parts_sets:
                if i in freq:
                    freq[i] += n
                else:
                    freq[i] = n
        return [f"{v} {k}" for k,v in freq.items()]