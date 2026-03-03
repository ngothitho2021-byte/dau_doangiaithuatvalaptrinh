class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range (len(nums)):
            count=0
            for j in range (len(nums)):
                if nums[j]<nums[i]:
                    count +=1
            a.append(count)   
        return a