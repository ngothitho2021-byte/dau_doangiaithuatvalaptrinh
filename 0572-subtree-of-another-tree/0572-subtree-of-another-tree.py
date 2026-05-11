# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        # Nếu cây tại node hiện tại giống subRoot thì trả về True
        if self.isSameTree(root, subRoot):
            return True
        
        # Nếu không, kiểm tra tiếp ở nhánh trái hoặc nhánh phải
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        # Nếu cả hai node đều rỗng thì giống nhau
            if not s and not t:
                return True
        # Nếu một node rỗng còn node kia không rỗng thì khác nhau
            if not s or not t:
                return False
        # Nếu giá trị khác nhau thì khác
            if s.val != t.val:
                return False
        # Kiểm tra tiếp cây con trái và phải
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)