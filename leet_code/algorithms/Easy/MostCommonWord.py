# 819. Most Common Word
'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.
'''

class Solution:
    # 32ms, Beats 97.83%
    # 17.39MB, Beats 6.13%
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        f = {}
        for i in "!?',;.":
            paragraph = paragraph.replace(i, ' ')

        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        
        for i in paragraph:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
                
        res = sorted(f.keys(), key=lambda x: f[x], reverse=True)
        
        for i in res:
            if not i in banned and i != "":
                return i
        return ""