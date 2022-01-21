# 14. Longest Common Prefix

'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPref = ""
        minimumLength = len(strs[0])  # temp shortest

        if strs is None or len(strs) == 0:
            return commonPref

        for i in range(1, len(strs)):
            # found shortest str
            minimumLength = min(minimumLength, len(strs[i]))

        for i in range(0, minimumLength):
            # use the first str to compare
            # [for firts str][position in str]
            currentChar = strs[0][i]

            # Check all other strings
            for j in range(0, len(strs)):
                # [for str][position in str]
                if strs[j][i] != currentChar:
                    return commonPref

            commonPref = commonPref + currentChar

        return commonPref
