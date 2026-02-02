class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dem = [0] * 26
        
        
        for ky_tu in s:
            dem[ord(ky_tu) - ord('a')] += 1
        
        
        for i in range(len(s)):
            if dem[ord(s[i]) - ord('a')] == 1:
                return i
        
        return -1