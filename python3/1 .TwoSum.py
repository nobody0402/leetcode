
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            if target - v in map:
                return map[target-v], i
            map[v] = i


if __name__ == "__main__":
    assert (0, 1) == Solution().twoSum([2, 7, 11, 15], 9)
