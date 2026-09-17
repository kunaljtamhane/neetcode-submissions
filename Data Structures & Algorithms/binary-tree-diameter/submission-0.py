# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0 #holds the maximum diameter found

    def calculateHeight(self, root):
        # Base Case: empty tree has height 0
        if not root:
            return 0
        # Recursively find height of left and right subtrees
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        # Update diameter path throught root uses leftHeight + rightHeight edges
        self.diameter = max(self.diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.calculateHeight(root)
        return self.diameter
        