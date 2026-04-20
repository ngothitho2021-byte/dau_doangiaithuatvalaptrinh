# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                # Nếu mid là lỗi, thì phiên bản lỗi đầu tiên nằm ở mid hoặc bên trái
                right = mid
            else:
                # Nếu mid không lỗi, thì phiên bản lỗi đầu tiên nằm bên phải
                left = mid + 1
        return left
        