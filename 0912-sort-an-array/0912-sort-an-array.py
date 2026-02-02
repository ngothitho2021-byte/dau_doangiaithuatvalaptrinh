class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSortInPlace(nums, 0, len(nums) - 1)
        return nums
    
    def mergeSortInPlace(self, nums, trai, phai):
        if trai >= phai:
            return
        
        giua = (trai + phai) // 2
        
        
        self.mergeSortInPlace(nums, trai, giua)
        self.mergeSortInPlace(nums, giua + 1, phai)
        
        
        self.merge(nums, trai, giua, phai)
    
    def merge(self, nums, trai, giua, phai):
        
        mang_trai = nums[trai:giua + 1]
        
        i = 0  
        j = giua + 1  
        k = trai  
        
       
        while i < len(mang_trai) and j <= phai:
            if mang_trai[i] <= nums[j]:
                nums[k] = mang_trai[i]
                i += 1
            else:
                nums[k] = nums[j]
                j += 1
            k += 1
        
        
        while i < len(mang_trai):
            nums[k] = mang_trai[i]
            i += 1
            k += 1