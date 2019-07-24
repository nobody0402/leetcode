class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        
        for i,x in enumerate(nums) :
            if i-x in hashMap:
                return hashMap[target-x], i
            
            hashMap[x] = i