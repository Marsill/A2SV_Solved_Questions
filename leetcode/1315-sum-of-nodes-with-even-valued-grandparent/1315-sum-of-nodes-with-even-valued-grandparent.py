# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def path(node, par, grand):
            nonlocal ans
            if  node == None or node.val == None:
                return 
            if grand != None:
                if grand.val % 2 ==0:
                    ans += node.val
                
            
            if node.left:
                path(node.left, node, par)
            if node.right:
                path(node.right, node, par)
        
        path(root, None, None)
        return ans