class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
      
        maxNumber = 0
        for i in range(length):
            slope ={}
            same = 1
            for j in range(i+1,length):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1] :
                        same +=1
                        continue
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                gcd = self.findGcd(x,y)
                t = (x/gcd,y/gcd)
                if t in slope:
                    slope[t] +=1
                else:
                    slope[t] = 1
            pm = max(slope.values()) if slope else 0    
            maxNumber = max(maxNumber,pm + same)
        
        return maxNumber    
            
    def findGcd(self,x,y):
        while y: 
            x, y = y, x % y 
        return x
                