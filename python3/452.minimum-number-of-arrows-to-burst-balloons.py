#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : x[1])

        cur_end = points[0][1]
        ar = 1
        for start, end in points[1:]:
            if start > cur_end:
                ar += 1
                cur_end = end

        return ar
# @lc code=end

