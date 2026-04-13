class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  loại bỏ phần tử trùng liên tiếp
        compressed = [nums[0]]
        for x in nums[1:]:
            if x != compressed[-1]:
                compressed.append(x)
    
        count = 0
        #  duyệt từ 1 đến len-2
        for i in range(1, len(compressed)-1):
            if compressed[i] > compressed[i-1] and compressed[i] > compressed[i+1]:
                count += 1  # hill
            elif compressed[i] < compressed[i-1] and compressed[i] < compressed[i+1]:
                count += 1  # valley
        return count