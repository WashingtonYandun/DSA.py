# 942. DI String Match
'''
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
'''


class Solution:
    # 74 ms, faster than 69.10%
    # 15.2 MB, less than 85.67%
    def diStringMatch(self, s: str) -> List[int]:
        izquierda = 0  # i use spanish in this one because its more intuitive
        derecha = len(s)

        result = []

        for i in s:
            if i == "I":
                result.append(izquierda)
                izquierda = izquierda + 1
            else:
                # if i == 'D'
                result.append(derecha)
                derecha = derecha - 1

        result.append(derecha)

        return result
