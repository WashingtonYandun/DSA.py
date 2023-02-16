# 1108. Defanging an IP Address
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
'''

class Solution:
    # 26 ms, faster than 95.78%
    # 13.8 MB, less than 48.22%
    def defangIPaddr(self, address: str) -> str:
        """
        Use replace method
        :param address: a valid ip string
        :return: the defanged string 
        """
        return address.replace(".", "[.]")