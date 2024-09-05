# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []
    
        current = root
        stack = []
        final = []
        stack.append([current.val])
        count = 0

        while stack:

            current_level = stack.pop()
            print(current_level)
            final.append(current_level)
            for current in current_level:
                if count % 2 == 0:
                    if current.right: stack.append(current.right)
                    if current.left: stack.append(current.left)
                if count % 2 != 0:
                    if current.left: stack.append(current.left)
                    if current.right: stack.append(current.right)
            count += 1

        return final
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Solution instance
sol = Solution()
output = sol.zigzagLevelOrder(root)
print(output)  # Expected output: [[1], [2, 3], [4, 5, 6], [7]]

