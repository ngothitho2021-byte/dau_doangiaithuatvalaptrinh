class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        total = 0
        for num, freq in count.items():
            if freq == 1:      # chỉ cộng nếu xuất hiện đúng 1 lần
             total += num
        return total