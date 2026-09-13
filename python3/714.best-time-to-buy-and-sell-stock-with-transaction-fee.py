#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     n = len(prices)
    #     dp = [[0]*2 for _ in range(n)]
    #     dp[0][0] = 0
    #     dp[0][1] = -prices[0]

    #     for i in range(1, n):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        
    #     return dp[-1][0]

    # This quicker use greedy approach, we can keep track of the minimum buying price 
    # and the profit we can make. 
    # If the current price is greater than the minimum buying price, 
    # we can sell and add to our profit. 
    # If the current price is less than the minimum buying price, 
    # we update the minimum buying price to be the current price plus the fee.
    def maxProfit(self, prices: List[int], fee: int) -> int:

        min_b = prices[0] + fee
        profit = 0
        for p in prices:
            if p > min_b:
                profit += p - min_b

                # Important: we need to update the min_b to be the current price,
                # because we can sell if the next price is higher.
                min_b = p
            else:
                min_b = min(min_b, p + fee)
        return profit
# @lc code=end

