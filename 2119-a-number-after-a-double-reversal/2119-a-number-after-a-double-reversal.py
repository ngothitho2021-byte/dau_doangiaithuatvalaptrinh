class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def reverse(x):
            dao = 0
            while x > 0:
                dao = dao * 10 + x % 10
                x //= 10
            return dao

        dao1 = reverse(num)
        dao2 = reverse(dao1)

        return dao2 == num