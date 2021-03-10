class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        smap = {}
        start = 0
        s_max = 0
        a = 0
        for a in range(len(s)):
            if s[a] in smap and smap[s[a]] >= start:
                s_max = max(s_max, a-start)
                start = smap[s[a]] + 1
                
            smap[s[a]] = a
            
        s_max = max(s_max, len(s) - start)
        
        return s_max
        