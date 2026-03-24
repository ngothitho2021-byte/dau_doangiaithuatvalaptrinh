class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time=0
        a=tickets[k]#so ve nguoi k can mua 
        for i in  range (len(tickets)) :
            if i<=k:
                time+=min(tickets[i],a)
            else:
                time+=min(tickets[i],a-1)
        return time