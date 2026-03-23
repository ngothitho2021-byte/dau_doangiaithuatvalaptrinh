class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()  # tập hợp lưu các chữ số duy nhất
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
    
        # Chuyển sang list và sắp xếp giảm dần
        sorted_digits = sorted(digits, reverse=True)
    
        # Nếu có ít nhất 2 chữ số thì trả về chữ số lớn thứ hai
        if len(sorted_digits) >= 2:
            return sorted_digits[1]
        else:
            return -1
