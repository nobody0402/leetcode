
'''Manacher算法'''
class Solution(object):
    def longestPalindrome(self, s):

        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        if len(s)<2:
            return s
        T='#'.join('@{}$'.format(s))#step 1
        #step2
        n=len(T)
        P=[0]*n
        c=0
        r=0
        maxlen=0
        centeridx=0
        for i in range(1,n-1):
            if r>i:
                P[i]=min(r-i,P[2*c-i])
          
            while T[i+1+P[i]]==T[i-1-P[i]]:
                P[i]=P[i]+1
     
            if i+P[i]>r:
                c=i
                r=i+P[i]
            if P[i]>maxlen:
                maxlen=P[i]
                centeridx=i
                
        begin=(centeridx-maxlen)//2
        end=(centeridx+maxlen)//2


        return s[begin:end]
            