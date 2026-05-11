class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1])  
        result = sign * rev
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result