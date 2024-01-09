# 939. Minimum Area Rectangle
'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
'''

class Solution:
    # 1064ms Beats, 55.63%
    # 17.56MB, Beats 30.06%
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        point_set = set(map(tuple, points))

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1] 
            for j in range(i+1, len(points) - 1):
                x2 = points[j][0]
                y2 = points[j][1]

                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0