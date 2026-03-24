# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dit = defaultdict(int)
        dit[0] = 1
        ans = 0
        def path(node, run):
            nonlocal ans
            if  node == None or node.val == None:
                return 
            upto = run + node.val
            count = upto - targetSum
            ans += dit[count] 
            dit[upto] += 1
            if node.left:
                path(node.left, upto)
            if node.right:
                path(node.right, upto)

            dit[upto] -= 1
        path(root, 0)
        return ans