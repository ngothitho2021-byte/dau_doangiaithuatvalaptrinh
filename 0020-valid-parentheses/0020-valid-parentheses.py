class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in mapping:  # nếu là ngoặc đóng
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:  # ngoặc mở
                stack.append(ch)
        
        return not stack