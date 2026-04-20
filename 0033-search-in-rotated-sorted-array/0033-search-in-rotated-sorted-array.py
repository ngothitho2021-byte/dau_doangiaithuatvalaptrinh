class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] == target:
                return mid
        
        # Kiểm tra nửa trái có sắp xếp không
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
            # Nửa phải sắp xếp
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
    
        return -1