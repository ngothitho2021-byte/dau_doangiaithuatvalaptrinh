class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import Counter
        s=Counter()
        for a in nums1:
            for b in nums2:
                s[a+b] +=1
        dem =0
        for c in nums3:
            for d in nums4:
                dem+=s[-(c+d)]
        return dem
