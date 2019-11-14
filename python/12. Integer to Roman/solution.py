class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [(1000,'M'),
                 (900,'CM'), 
                 (500,'D'),
                 (400,'CD'),
                 (100,'C'),
                 (90,'XC'),
                 (50,'L'),
                 (40,'XL'),
                 (10,'X'),
                 (9,'IX'),
                 (5,'V'),
                 (4,'IV'),
                 (1,'I')]
                                                                                           
                                                                                           
        result = ''
        for t in roman :
            d,num = divmod(num,t[0])
            result += t[1]*d

            if not num:
                break
        
        return result