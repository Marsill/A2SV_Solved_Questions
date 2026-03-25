# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        N = len(postorder)
        post = {}
        
        for j in range(len(postorder)):
            post[postorder[j]] = j

        def construct(i1, i2, j1):
            if i1 > i2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1+1]

                mid = post[left_val]

                left_size = mid - j1 + 1

                root.left = construct(i1+1, i1 + left_size, j1)
                root.right = construct(i1 + left_size + 1, i2, mid+1)

            return root
        return construct(0, N-1, 0)
            