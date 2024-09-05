# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):

        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:

            level = []

            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(level)

        return result
    
# Manually constructing the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.right = TreeNode(7)

# Solution instance
sol = Solution()
output = sol.levelOrder(root)
print(output)  # Expected output: [[1], [2, 3], [4, 5, 6], [7]]
