class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        chars = list(word)  # chuyển chuỗi thành list
        idx = -1
        for i in range(len(chars)):
            if chars[i] == ch:
                idx = i
                break
        
        if idx == -1:
            return word
        
        # đảo ngược đoạn từ 0 đến idx
        left, right = 0, idx
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return "".join(chars)  # ghép list thành chuỗi