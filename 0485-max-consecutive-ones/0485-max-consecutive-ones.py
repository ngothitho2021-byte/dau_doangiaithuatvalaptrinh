class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_dem = 0  
        dem_hien_tai = 0  
        for num in nums:
            if num == 1:
                
                dem_hien_tai += 1
                
                max_dem = max(max_dem, dem_hien_tai)
            else:
               
                dem_hien_tai = 0
        
        return max_dem