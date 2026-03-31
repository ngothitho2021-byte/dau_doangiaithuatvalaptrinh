class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits=list(map(int,str(num)))# digits chuyển số nguyên thành chuỗi ,sau đó tách các ký tự thành số nguyên
        digits.sort()#sắp xếp theo thứ tự tăng dần
        new1,new2=" ",""# khởi tạo chuỗi rỗng
        for i,d in enumerate(digits):
            if i%2==0:
                new1+=str(d)
            else:
                new2+=str(d)
        return int(new1)+int(new2)