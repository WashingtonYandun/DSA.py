# 1816. Truncate Sentence
'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).
For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.
'''


class Solution:
    # 30 ms, faster than 89.87%
    # 13.8 MB, less than 61.06%
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        return " ".join(s[:k])
