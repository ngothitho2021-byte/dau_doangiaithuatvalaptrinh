class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for w in words:
        # Hàm startswith kiểm tra xem chuỗi w có bắt đầu bằng pref không
            if w.startswith(pref):
                count += 1
        return count
        