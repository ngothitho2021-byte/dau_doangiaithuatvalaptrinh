# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev = None  # lưu giá trị node trước đó khi duyệt inorder

        def inorder(node):
            if not node:
                return True
            # duyệt cây con trái
            if not inorder(node.left):
                return False
            # kiểm tra điều kiện BST
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            # duyệt cây con phải
            return inorder(node.right)

        return inorder(root)
           