// 0 ms | 22.7 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def depth(root):
            if not root:
                return -1
            return max(depth(root.left), depth(root.right))+1
        ans = depth(root)+1
        return ans