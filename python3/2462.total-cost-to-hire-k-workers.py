#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2 * candidates + k > len(costs):
            costs.sort()
            return sum(costs[:k])
            
        left = candidates
        right = len(costs) - candidates - 1

        heap_left = costs[:left]
        heap_right = costs[right + 1:]

        heapq.heapify(heap_left)
        heapq.heapify(heap_right)

        total = 0
        for _ in range(k):
            if heap_left[0] <= heap_right[0]:
                total += heapq.heapreplace(heap_left, costs[left])
                left += 1
            else:
                total += heapq.heapreplace(heap_right, costs[right])
                right -= 1

        return total
