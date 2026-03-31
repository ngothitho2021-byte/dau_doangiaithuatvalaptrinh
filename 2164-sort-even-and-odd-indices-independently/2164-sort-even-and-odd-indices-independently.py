class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        chan=[nums[i] for i in range(0,len(nums),2)]
        le=[nums[i] for i in range(1,len(nums),2)]
        chan.sort()
        le.sort(reverse=True)
        result=[]
        c,l=0,0
        for i in range(len(nums)):
            if i%2==0:
                result.append(chan[c])
                c+=1
            else :
                result.append(le[l])
                l+=1   
        return result