# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def helper(self, root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            
            # print(len(deque([root])))
            val = root.val

            if val <= lower or val >= upper:
                 return False

            if not self.helper(root.right, val, upper):
                return False
            if not self.helper(root.left, lower, val):
                return False
            
            return True
        
solution = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(solution.helper(root, lower=float('-inf'), upper=float('inf')))  #True
