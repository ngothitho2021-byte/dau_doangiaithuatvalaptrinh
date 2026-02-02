class Solution:
    def pivotIndex(self, nums):
        
        tong_toan_bo = sum(nums)
        tong_trai = 0
        
        
        for i in range(len(nums)):
           
            tong_phai = tong_toan_bo - tong_trai - nums[i]
            
           
            if tong_trai == tong_phai:
                return i
            
            
            tong_trai += nums[i]
        
        
        return -1