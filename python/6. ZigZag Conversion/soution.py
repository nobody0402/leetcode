
# 找出每一行的規則為 k + 2 * (n-k-1) + 2k + 2 * (n-k-1) + 2k ....
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) < numRows  :
            return s
        
        result = ''
        
        for i in range(numRows):
            offset1 = 2*(numRows - i -1)
            offset2 = 2*i
            index = i
            
            result += s[index]
            while index < len(s):
                if offset1 > 0:
                    index += offset1
                    if index < len(s) :
                        result += s[index]
                
                if offset2 > 0:
                    index += offset2
                    if index < len(s) :
                        result += s[index]
                        
        return result

#每個Row用一個陣列暫存，用方向來決定該放入哪一行，碰到邊界則轉向
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        a = [''] * numRows 
        
        step = 1
        idx = 0
        for c in s:
            a[idx] += c
            
            if idx == 0:
                step = 1
            elif idx == numRows -1 :
                step = -1
                        
            idx += step
                        
        return ''.join(a)