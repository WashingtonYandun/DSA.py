# 2942. Find Words Containing Character
'''
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
'''

class Solution:
    # 64ms Beats 71.32%
    # 17.49MB Beats 19.27%
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        flag = False
        res = []
        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if words[i][j] == x and not flag:
                    res.append(i)
                    flag = True    
            flag = False
        return res