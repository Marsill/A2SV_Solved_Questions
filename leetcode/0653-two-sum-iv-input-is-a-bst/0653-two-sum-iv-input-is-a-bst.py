# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        two_sum = defaultdict(int)

        def find_t(node):
            if not node:
                return False
            diff = k - node.val

            if diff in two_sum:
                return True
            else:
                two_sum[node.val] += 1
            return find_t(node.right) or find_t(node.left)

        return find_t(root)