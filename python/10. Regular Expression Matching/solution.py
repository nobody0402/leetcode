class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        m = len(s)+1
        n = len(p)+1
        
        dp = [[False for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = True
        
        for j in range(2, n):
             if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  
                
        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]== '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                elif p[j-1] == '.' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                
                
        return dp[m-1][n-1]