#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m

        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        
        for y in range(1,m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        
        return dp[-1][-1]

        
        
# @lc code=end

