class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem=0
        for i in nums:
            so_chu_so=len(str(i))
            if so_chu_so %2==0:
                dem+=1
        return dem