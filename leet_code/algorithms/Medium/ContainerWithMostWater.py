# 11. Container With Most Water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    # 530ms, Beats 93.49%
    # 30.02MB, Beats 10.10%
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        most = 0

        while l <= r:
            h_l = height[l]
            h_r = height[r]

            most = max(most, (r - l) * min(h_l, h_r))

            if h_l < h_r:
                l += 1
            else:
                r -= 1

        return most

