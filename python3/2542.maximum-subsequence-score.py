#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_indices = sorted(range(len(nums2)), key=lambda i: -nums2[i])

        nums1_sorted = [nums1[i] for i in sorted_indices]
        nums2_sorted = [nums2[i] for i in sorted_indices]
        n = len(nums1)
        min_heap = nums1_sorted[:k]
        heapq.heapify(min_heap)
        sum_nums1 = sum(min_heap)
        max_score = sum_nums1 * nums2_sorted[k - 1]
        for i in range(k, n):
            num1, num2 = nums1_sorted[i], nums2_sorted[i]
            sum_nums1 += num1
            heapq.heappush(min_heap, num1)
            sum_nums1 -= heapq.heappop(min_heap)
            max_score = max(max_score, sum_nums1 * num2)

        return max_score
        
# @lc code=end

