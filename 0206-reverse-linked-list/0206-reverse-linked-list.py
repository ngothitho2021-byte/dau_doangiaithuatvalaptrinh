# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next   # Lưu nút tiếp theo
            curr.next = prev        # Đảo chiều liên kết
            prev = curr             # Di chuyển prev lên curr
            curr = next_temp        # Di chuyển curr sang nút tiếp theo
        return prev