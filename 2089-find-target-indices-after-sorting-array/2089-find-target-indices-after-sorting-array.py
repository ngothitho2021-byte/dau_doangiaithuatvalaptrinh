class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)  


        result = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                result.append(i)
        return result 