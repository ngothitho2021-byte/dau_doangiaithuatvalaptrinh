class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box = {}  # Dictionary lưu số lượng bóng trong mỗi hộp (key = tổng chữ   số, value = số bóng)

    # Duyệt qua tất cả các số từ lowLimit đến highLimit
        for num in range(lowLimit, highLimit+1):
        # Tính tổng chữ số của số num
            s = sum(map(int, str(num)))  

        # Nếu hộp với tổng chữ số s chưa tồn tại thì tạo mới
            if s not in box:
                box[s] = 0

        # Thêm một quả bóng vào hộp có tổng chữ số s
            box[s] += 1

    # Trả về số lượng bóng nhiều nhất trong một hộp
        return max(box.values())