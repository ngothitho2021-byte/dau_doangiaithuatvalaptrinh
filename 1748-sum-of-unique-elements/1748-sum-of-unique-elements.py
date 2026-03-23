class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        
        count = {}   # Dictionary dùng để lưu số lần xuất hiện của từng phần tử
    # Duyệt qua từng phần tử trong mảng nums
        for i in nums:
            if i not in count:   # Nếu phần tử chưa có trong dictionary thì khởi tạo
                count[i] = 0
            count[i] += 1        # Tăng số lần xuất hiện của phần tử đó lên 1

        total = 0   # Biến lưu tổng các phần tử duy nhất
    # Duyệt qua từng cặp (num, freq) trong dictionary
        for num, freq in count.items():
            if freq == 1:        # Nếu phần tử chỉ xuất hiện đúng 1 lần
                total += num     # Cộng giá trị của phần tử đó vào tổng

        return total  # Trả về kết quả cuối cùng