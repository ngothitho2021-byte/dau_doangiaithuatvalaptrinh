# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Di chuyển first đi trước n+1 bước
        for _ in range(n+1):
            first = first.next
        
        # Di chuyển cả hai cho đến khi first đến cuối
        while first:
            first = first.next
            second = second.next
        
        # Xóa nút thứ n từ cuối
        second.next = second.next.next
        
        return dummy.next