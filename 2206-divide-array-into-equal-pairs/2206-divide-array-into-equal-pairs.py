class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
    
        # kiểm tra tất cả tần suất có chẵn không
        for count in freq.values():
            if count % 2 != 0:
                return False
        return True