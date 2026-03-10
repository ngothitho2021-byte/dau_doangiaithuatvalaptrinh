class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        
        s=[0]*num_people
        i =0
        while candies>0:
            give=min(candies,i+1)
            s[i%num_people]+=give
            candies-=give
            i+=1
        return s