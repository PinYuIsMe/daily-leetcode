# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    diameter = 0

    def findD(self, r):
        left, right = 0, 0
        if r.val == "null":
            return 0
        
        if r.left:
            left = self.findD(r.left) + 1
        if r.right:
            right = self.findD(r.right) + 1
        
        self.diameter = max(self.diameter, left + right)

        return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = max(self.findD(root), self.diameter)

        return self.diameter

        
