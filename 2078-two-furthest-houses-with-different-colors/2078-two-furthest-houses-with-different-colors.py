class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        n=len(colors)#so ngoi nha (do dai mang)
        max_dist=0#bien luu khoan cach lon nhat
        for i in range (n-1,-1,-1):#duyet tu nha cuoi cung ve nha  dau tien 
            if colors[i]!=colors[0]:#tim ngoi nha khac voi nha so 0
                max_dist= max(max_dist,i-0)#cap nhat khoang cach cua ngoi nha 
                break
        for i in range (n):#duyet tu nha dau tien den nha cuoi cung
            if colors[i]!=colors[n-1]:#tim ngoi nha kgac voi nha cuoi cung 
                max_dist=max(max_dist,(n-1)-i)#cap nhat khoang cach
                break
        return max_dist#tra ve gia tri lon