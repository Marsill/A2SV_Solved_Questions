# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def distribute(node):
            if not node:
                return 0
            
            l_extra = distribute(node.left)
            r_extra = distribute(node.right)

            extra_coins = l_extra + r_extra + node.val - 1
            self.ans += abs(extra_coins)

            return extra_coins

        distribute(root)
        return self.ans