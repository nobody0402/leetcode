class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
   
        str = str.strip()
    
        if not str :
            return 0
        
        sign = 1
        number = 0
        if str[0] == '+' :
            str = str[1:]
        elif str[0] == '-' :
            str = str[1:]
            sign = -1
        
        result = ''
        for s in str:
            if s.isdigit():
                result+=s
            else:
                break
                
        number = sign * int(result) if result else number       
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number
        