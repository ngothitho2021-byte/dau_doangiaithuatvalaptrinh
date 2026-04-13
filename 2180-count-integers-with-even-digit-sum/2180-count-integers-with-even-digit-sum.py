class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def digit_sum(x):
            return sum(int(d) for d in str(x))
    
        count = 0
        for i in range(1, num+1):
            if digit_sum(i) % 2 == 0:
                count += 1
        return count