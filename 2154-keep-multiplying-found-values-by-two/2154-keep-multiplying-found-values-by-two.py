class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        a=set(nums)# kiểm tra phần tử không trùng lặp 
        while original in a :
            original*=2
        return original
                
