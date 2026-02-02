class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        count=0
        for ch in reversed(s):
            if ch !=" ":
                count +=1
            else: 
                break
        return count