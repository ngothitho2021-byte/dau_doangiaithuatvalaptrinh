class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem=0
        a=max(nums)
        b=min(nums)
        for i in nums:
            if b<i<a:
                dem+=1
        return dem