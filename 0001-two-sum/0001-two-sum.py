class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s={}
        for i in range (len(nums)):
            need=target-nums[i]
            if need in s:
                return [s[need],i]
            s[nums[i]]=i
        