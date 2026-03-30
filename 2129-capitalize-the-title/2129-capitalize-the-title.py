class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        n=(title.split())
        result=[]
        for i in n:
            if len(i)<=2:
                result.append(i.lower())
            else:
                result.append(i[0].upper()+i[1:].lower())
        return " ".join(result)