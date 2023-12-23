# 692. Top K Frequent Words
'''
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''

class Solution:
    # 58ms, Beats 86.51%
    # 17.40MB, Beats 12.78%
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f = {}

        for i in words:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        
        return sorted(f.keys(), key=lambda x: (-f[x], x))[:k]