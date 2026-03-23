class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_height=0#độ cao hiện tại,bắt đầu bằng 0
        max_height=0#độ cao lớn nhất khởi tạo bằng 0
        for i in gain:# cho vòng lặp duyệt từng mảng 
            current_height+=i# cộng thêm sau mỗi lần duyệt 
            max_height = max(max_height, current_height)#so sánh độ cao hiện tại và độ cao lớn nhất
        return max_height

        

        