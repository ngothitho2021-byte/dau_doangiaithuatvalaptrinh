class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        co_mat = set(nums)
        
        
        ket_qua = []
        for i in range(1, len(nums) + 1):
            if i not in co_mat:
                ket_qua.append(i)
        
        return ket_qua