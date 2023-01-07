
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        k = int((m + n + 1) / 2)

        l = 0
        r = m

        while l < r:
            mid1 = int(l + (r - l) / 2)
            mid2 = k - mid1
            if nums1[mid1] < nums2[mid2 - 1]:
                l = mid1+1
            else:
                r = mid1

        m1 = l
        m2 = k - l

        c1 = max(-1 if m1 <= 0 else nums1[m1 - 1],
                 -1 if m2 <= 0 else nums2[m2 - 1])

        if (m+n) % 2 == 1:
            return c1

        c2 = min(float('int') if m1 >= m else nums1[m1],
                 float('int') if m2 >= n else nums2[m2])

        return (c1 + c2) / 2


class RecursiveSolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        odd = (m+n) & 1
        median = int((m+n+1) / 2)

        if odd:
            return Solution.findMedian(nums1, nums2, median)
        else:
            return (Solution.findMedian(nums1, nums2, median) + Solution.findMedian(nums1, nums2, int((m+n+2) / 2)))/2.0

    def findMedian(n1: List[int], n2: List[int], k: int):
        if not n1:
            return n2[k-1]
        if not n2:
            return n1[k-1]
        if k == 1:
            return min(n1[0], n2[0])
        i = min(len(n1), int(k/2))
        j = min(len(n2), k - i)

        if n1[i-1] > n2[j-1]:
            return Solution.findMedian(n1, n2[j:], k-j)
        else:
            return Solution.findMedian(n1[i:], n2, k-i)


if __name__ == "__main__":
    assert 2.0 == Solution().findMedianSortedArrays([1, 3], [2])
