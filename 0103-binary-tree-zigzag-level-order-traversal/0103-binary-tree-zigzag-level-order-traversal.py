# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # cờ để biết tầng này duyệt trái→phải hay phải→trái
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Nếu tầng này cần đảo ngược thì đảo list
            if not left_to_right:
                level.reverse()
            
            result.append(level)
            left_to_right = not left_to_right  # đổi chiều cho tầng tiếp theo
        
        return result