class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        a=len(arr)
        b=arr.count(0)
        i=a-1
        j=a+b-1
        while i<j:
            if j<a:
                arr[j]=arr[i]
            if arr[i]==0:
                j-=1
                if j<a:
                    arr[j]=0
            i-=1
            j-=1


        