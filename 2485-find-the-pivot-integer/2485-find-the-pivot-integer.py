class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2
        for x in range(1, n + 1):
            left_sum = x * (x + 1) // 2
            right_sum = total - left_sum + x
            if left_sum == right_sum:
                return x
        return -1