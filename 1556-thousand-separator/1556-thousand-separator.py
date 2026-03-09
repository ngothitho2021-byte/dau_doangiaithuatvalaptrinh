class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s= str(n)
        parts = []
        while len(s)>3:
            parts.insert(0,s[-3:])
            s = s[:-3]               
        parts.insert(0, s)          
        return ".".join(parts)


        