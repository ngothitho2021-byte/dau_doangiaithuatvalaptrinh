class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        a=numBottles
        b=numBottles
        while b>=numExchange:
            n=b//numExchange
            a+=n
            b=b%numExchange+n
        return a
        