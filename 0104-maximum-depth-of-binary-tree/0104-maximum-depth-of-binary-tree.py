# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([root])   # Khởi tạo hàng đợi với nút gốc
        depth = 0
        while queue:            # Lặp cho đến khi hàng đợi rỗng
            for _ in range(len(queue)):   # Duyệt hết một tầng
                node = queue.popleft()    # Lấy nút ra khỏi hàng đợi
                if node.left:             # Nếu có con trái → thêm vào hàng đợi
                    queue.append(node.left)
                if node.right:            # Nếu có con phải → thêm vào hàng đợi
                    queue.append(node.right)
            depth += 1         # Sau khi duyệt xong một tầng → tăng độ sâu
        return depth