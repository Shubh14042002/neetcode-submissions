# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root == None:
            return 0
        else :
            count+=1
        
        left_count = self.maxDepth(root.left)

        
        right_count = self.maxDepth(root.right)

        return count + max(left_count,right_count)

