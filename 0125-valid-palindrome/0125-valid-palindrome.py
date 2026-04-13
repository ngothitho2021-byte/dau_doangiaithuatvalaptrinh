class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            # bỏ ký tự không phải chữ cái/số
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            # so sánh sau khi chuyển về chữ thường
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True