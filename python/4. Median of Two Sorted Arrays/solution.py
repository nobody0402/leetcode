class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0
        i = -1
        charDict = {}
        for j in range(len(s)):
            if s[j] not in charDict or  charDict[s[j]]< i:
                charDict[s[j]] = j
                ans = max(ans,j-i)
            else:
                i = charDict[s[j]]
                charDict[s[j]] = j

        return ans
            