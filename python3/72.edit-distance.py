#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
from collections import deque


class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]

    #     for i in range(m + 1):
    #         dp[i][0] = i
    #     for j in range(n + 1):
    #         dp[0][j] = j

    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1]
    #             else:
    #                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    #     return dp[m][n]

    # Space optimized version
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
        
    #     # dp 陣列初始化為第一列 (word1 為空字串時)
    #     dp = list(range(n + 1))
        
    #     for i in range(1, m + 1):
    #         prev = dp[0]        # 記錄左上角 dp[i-1][0]
    #         dp[0] = i           # 第 0 欄：word2 為空，刪除 i 次
            
    #         for j in range(1, n + 1):
    #             temp = dp[j]    # 暫存覆蓋前的正上方值，作為下一輪的左上角
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[j] = prev
    #             else:
    #                 dp[j] = 1 + min(dp[j], dp[j - 1], prev)
    #             prev = temp
                
    #     return dp[n]

    # best performance BFS
    def minDistance(self, word1: str, word2: str) -> int:
        q, visited = deque(), set()
        m, n = len(word1), len(word2)

        q.append((0,0))
        op = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                while i < m and j < n and word1[i] == word2[j]:
                    i += 1
                    j += 1

                if i == m and j == n:
                    return op
            
                if i < m:
                    q.append((i + 1, j))
                if j < n:
                    q.append((i, j + 1))
                if i < m and j < n:
                    q.append((i + 1, j + 1))
            op += 1

        return op
# @lc code=end

