# 2114. Maximum Number of Words Found in Sentences
'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
'''


class Solution:
    # 40 ms, faster than 93.61%
    # 13.8 MB, less than 99.30%
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for i in sentences:
            i = i.split(" ")
            lenght = len(i)
            if lenght > max_words:
                max_words = lenght

        return max_words
