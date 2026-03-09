import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        counts = Counter(word for word in words if word not in banned_set)
        return counts.most_common(1)[0][0]
      
        
