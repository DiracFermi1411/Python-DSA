# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while stack or current:
            # Traverse left subtree
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            result.append(current.val)

            # Traverse right subtree
            current = current.right

        return result

