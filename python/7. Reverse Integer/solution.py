class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = int(str(abs(x))[::-1])
        
        result = result if x > 0 else -result
                
        return result if  -2147483648 <= result <= 2147483648 else 0
        