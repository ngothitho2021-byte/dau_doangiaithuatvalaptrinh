class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        for x in nums:
        # Nếu khoảng cách nhỏ hơn, hoặc bằng nhưng giá trị lớn hơn
            if abs(x) < abs(closest) or (abs(x) == abs(closest) and x > closest):
             closest = x
        return closest