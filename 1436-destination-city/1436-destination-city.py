class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start=set()
        end=set()
        for a,b in paths:
            start.add(a)
            end.add(b)
        for i in end:
            if i not in start:
                return i