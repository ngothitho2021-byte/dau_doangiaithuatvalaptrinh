class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(1, len(s), 2):  # duyệt qua các vị trí lẻ
            c = s[i-1]                 # ký tự trước đó
            x = int(s[i])              # chữ số tại vị trí i
            s[i] = chr(ord(c) + x)   
        return "".join(s)
