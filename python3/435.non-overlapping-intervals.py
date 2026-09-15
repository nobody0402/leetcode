#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    # DP solution
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     n = len(intervals)
    #     dp = [1] * n
    #     intervals.sort(key=lambda x: x[0])
    #     for i in range(1, len(intervals)):
    #         for j in range(i):
    #             if intervals[j][1] <= intervals[i][0]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return len(intervals) - dp[n]


    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        last_end = intervals[0][1]
        kept = 1
        for interval in intervals[1:]:
            if interval[0] >= last_end:
                kept+=1
                last_end = interval[1]
            
        return n - kept 
# @lc code=end

