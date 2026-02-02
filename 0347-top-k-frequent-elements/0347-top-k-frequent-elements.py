class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s={}
        for i in nums:
            if  i in s:
                s[i]+= 1
            else:
                s[i]=1
        result=[]
        for i in range(k):
            max_count=0
            max_number=None
            for key,value in s.items():
                if value>max_count:
                    max_count=value
                    max_number=key
            result.append(max_number)
            del s[max_number]
        return result