#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d = (a | b) ^ c

        e = a & b & d

        return d.bit_count() + e.bit_count()
        
# @lc code=end

