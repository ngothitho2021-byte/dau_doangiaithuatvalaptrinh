class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s=""
        for i in range (len(strs[0])):
            char=strs[0][i]
            for d in strs :
                if i>=len(d ) or d[i]!=char:
                    return s
            s+=char
        return s