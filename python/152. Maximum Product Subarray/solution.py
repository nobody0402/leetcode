class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        res = maxNum = minNum = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] < 0 :
                maxNum,minNum = minNum,maxNum
            
            maxNum = max(nums[i],nums[i]*maxNum)
            minNum = min(nums[i],nums[i]*minNum)
            
            res = max(maxNum,res)
        
        return res
        
        