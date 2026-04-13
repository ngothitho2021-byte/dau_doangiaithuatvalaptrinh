class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        freq = {}
        n = len(nums)
        for i in range(n-1):
            if nums[i] == key:
                target = nums[i+1]
                freq[target] = freq.get(target, 0) + 1
    
    # tìm target có tần suất lớn nhất
        return max(freq, key=freq.get)
        