class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = sorted(zip(names, heights), key=lambda x: x[1],      reverse=True)
        return [name for name, _ in people]
