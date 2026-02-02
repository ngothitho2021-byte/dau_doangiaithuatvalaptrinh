class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        s = Counter(magazine)
        v = Counter(ransomNote)
        for ch in v : 
            if v[ch] >s[ch]:
                return False 
        else : 
            return True