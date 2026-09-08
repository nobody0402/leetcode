#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1] + [0] * n


        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
        
        return ans[n]
        
# @lc code=end

