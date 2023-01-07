from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

    def manacher(self, s: str) -> str:

        t = "#".join(f"@{s}$")
        n = len(t)
        p = [0] * n

        r = 0
        centerid = 0
        maxlen = 0
        maxcenteridx = 0
        for i in range(1, n - 1):
            if r > i:
                p[i] = min(r - i, p[centerid * 2 - i])

            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] = p[i] + 1

            if r < i + p[i]:
                r = i + p[i]
                centerid = i

            if maxlen < p[i]:
                maxlen = p[i]
                maxcenteridx = i

        begin = (maxcenteridx - maxlen) // 2
        end = (maxcenteridx + maxlen) // 2

        return s[begin:end]
