#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    # Base Cases:
    # f(1) = 1, f(2) = 2, f(3) = 5
    #
    # Derivation:
    # Let f(n) be fully covered boards, g(n) be boards with 1 square missing:
    #   1) f(n)   = f(n-1) + f(n-2) + 2*g(n-1)  (vertical, 2 horizontals, or L-trominoes)
    #   2) g(n)   = f(n-2) + g(n-1)
    #
    # Subtracting f(n-1) from f(n):
    #   f(n) - f(n-1) = f(n-1) - f(n-3) + 2*(g(n-1) - g(n-2))
    # Since g(n-1) - g(n-2) = f(n-3):
    #   f(n) - f(n-1) = f(n-1) + f(n-3)
    #   => f(n) = 2*f(n-1) + f(n-3)
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        d1,d2,d3 = 1,2,5

        for _ in range(3, n):
            current = d1 + d3*2

            d1, d2, d3 = d2,d3,current
        
        return d3 % (10**9+7)
        
# @lc code=end

