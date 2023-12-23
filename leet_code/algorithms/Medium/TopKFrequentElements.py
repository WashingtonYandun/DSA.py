# 347. Top K Frequent Elements
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    # 83ms, Beats 98.77%
    # 21.92MB, Beats 19.42%
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frec = {}
        
        for i in nums:
            if i in frec:
                frec[i] += 1
            else:
                frec[i] = 1
                
        sor = sorted(frec.keys(), key=lambda x: frec[x], reverse=True)[:k]
        return sor[:k]