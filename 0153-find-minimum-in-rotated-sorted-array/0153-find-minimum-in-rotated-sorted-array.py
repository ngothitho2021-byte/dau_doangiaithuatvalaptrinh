class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
        # Nếu mid lớn hơn phần tử cuối, min nằm bên phải
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
            # Ngược lại, min nằm bên trái hoặc chính mid
                right = mid
    
        return nums[left]