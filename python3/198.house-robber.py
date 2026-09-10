# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0], dp[1] = nums[0], nums[1]


#         for i in range(2, n):
#             dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
#         return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for num in nums:
            current = max(prev1, prev2+num)
            prev2 = prev1
            prev1 = current
        
        return prev1