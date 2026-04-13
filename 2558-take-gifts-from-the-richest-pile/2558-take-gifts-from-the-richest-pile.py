class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        
        import heapq
        import math

        # Dùng heap âm để mô phỏng max-heap
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)   # lấy phần tử lớn nhất
            reduced = int(math.sqrt(largest))  # thay vì math.isqrt
            heapq.heappush(heap, -reduced)

        return -sum(heap)