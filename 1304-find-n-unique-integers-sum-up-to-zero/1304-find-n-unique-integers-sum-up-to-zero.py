class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==1:
            return [0]
        a=[]
        for i in range(1,n//2+1):
            a.append(i)
            a.append(-i)
        if n%2==1:
            a.append(0) 
        return a