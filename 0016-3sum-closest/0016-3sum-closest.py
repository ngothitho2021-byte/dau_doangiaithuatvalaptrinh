class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        res = 0
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < closest:
                    closest = abs(s - target)
                    res = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s  # nếu bằng target thì trả về ngay
        return res