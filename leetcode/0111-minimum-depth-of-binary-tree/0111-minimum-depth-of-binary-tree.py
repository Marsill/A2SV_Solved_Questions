# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def mini(node):
            if not node:
                return 0

            if not node.right:
                return 1 + mini(node.left)
            if not node.left:
                return 1 + mini(node.right)
            
            else:
                return min(1 + mini(node.left), 1 + mini(node.right))
                
        return mini(root)