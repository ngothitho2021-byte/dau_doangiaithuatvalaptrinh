class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s={}
        for i in strs:
            key="".join(sorted(i))
            if key not in s:
                s[key]=[]
            s[key].append(i)
        return list(s.values())
            
        