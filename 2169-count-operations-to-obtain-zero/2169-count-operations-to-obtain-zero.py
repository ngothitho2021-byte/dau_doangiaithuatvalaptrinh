class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        a=0
        while num1>0 and num2>0:
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
            a+=1
        return a
